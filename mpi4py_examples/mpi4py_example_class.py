# -*- coding: utf-8 -*-
"""
================================
Evaluate the mpy4py functionality
================================

MPI for Python supports convenient, pickle-based communication
of generic Python object as well as fast, near C-speed,
direct array data communication of buffer-provider objects
(e.g., NumPy arrays).


Running Python scripts with MPI
Usage:
        $ mpiexec -n 4 python mpi4py_example_class.py

THe Sphinx docstring format:

'''[Summary]

:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
''''
"""
from __future__ import division
from __future__ import print_function

from mpi4py import MPI
import numpy
import mmap

import pprint


class MPI4PY_EVALUATION:

    def __init__(self) -> None:
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank()
        self.size = self.comm.Get_size()


    def point_to_point_communication(self):
        """Python objects (pickle under the hood)"""
        if self.rank == 0:
            data = {'a': 7, 'b': 3.14}
            print(self.comm.send(data, dest=1, tag=11))

        elif self.rank == 1:
            data = self.comm.recv(source=0, tag=11)
            print(data)

    def point_to_point_communication_non_blocking(self):
        """Python objects with non-blocking communication"""
        if self.rank == 0:
            data = {'a': 7, 'b': 3.14}
            req = self.comm.isend(data, dest=1, tag=11)
            print(req)
            req.wait()
        elif self.rank == 1:
            req = self.comm.irecv(source=0, tag=11)
            print(req)
            data = req.wait()

    def point_to_point_communication_using_numpy(self):
        """NumPy arrays (the fast way!)"""
        # passing MPI datatypes explicitly
        if self.rank == 0:
            data = numpy.arange(1000, dtype='i')
            self.comm.Send([data, MPI.INT], dest=1, tag=77)
        elif self.rank == 1:
            data = numpy.empty(1000, dtype='i')
            self.comm.Recv([data, MPI.INT], source=0, tag=77)

        # automatic MPI datatype discovery
        if self.rank == 0:
            data = numpy.arange(100, dtype=numpy.float64)
            print(self.comm.Send(data, dest=1, tag=13))

        elif self.rank == 1:
            data = numpy.empty(100, dtype=numpy.float64)
            print(self.comm.Recv(data, source=0, tag=13))

    def broadcasting(self):
        """NumPy arrays (the fast way!)"""
        if self.rank == 0:
            data = {'key1' : [7, 2.72, 2+3j],
                    'key2' : ( 'abc', 'xyz')}
        else:
            data = None
        data = self.comm.bcast(data, root=0)
        print(data)


    def scattering(self):
        """NumPy arrays (the fast way!)"""
        if self.rank == 0:
            data = [(i+1)**2 for i in range(self.size)]
        else:
            data = None
        data = self.comm.scatter(data, root=0)
        print(data)
        assert data == (self.rank+1)**2


    def gathering(self):
        """NumPy arrays (the fast way!)"""
        data = (self.rank+1)**2
        data = self.comm.gather(data, root=0)
        if self.rank == 0:
            for i in range(self.size):
                assert data[i] == (i+1)**2
        else:
            assert data is None


    def broadcasting_a_numpy_array(self):
        """NumPy arrays (the fast way!)"""
        if self.rank == 0:
            data = numpy.arange(100, dtype='i')
        else:
            data = numpy.empty(100, dtype='i')
        self.comm.Bcast(data, root=0)
        for i in range(100):
            assert data[i] == i


    def scattering_a_numpy_array(self):
        """Scattering NumPy arrays"""
        sendbuf = None
        if self.rank == 0:
            sendbuf = numpy.empty([self.size, 100], dtype='i')
            sendbuf.T[:,:] = range(self.size)
        recvbuf = numpy.empty(100, dtype='i')
        self.comm.Scatter(sendbuf, recvbuf, root=0)
        assert numpy.allclose(recvbuf, self.rank)

    def gathering_a_numpy_array(self):
        """Gathering NumPy arrays"""
        sendbuf = numpy.zeros(100, dtype='i') + self.rank
        recvbuf = None
        if self.rank == 0:
            recvbuf = numpy.empty([size, 100], dtype='i')
        self.comm.Gather(sendbuf, recvbuf, root=0)
        if rself.ank == 0:
            for i in range(self.size):
                assert numpy.allclose(recvbuf[i,:], i)

    def parallel_matrix_vector_product(self, A, x):
        """Parallel matrix-vector product"""
        m = A.shape[0] # local rows
        p = self.comm.Get_size()
        xg = numpy.zeros(m*p, dtype='d')
        self.comm.Allgather([x,  MPI.DOUBLE], [xg, MPI.DOUBLE])
        y = numpy.dot(A, xg)
        return y

    def hello_world(self):
        """Helo world"""
        print("Hello! I'm rank %d from %d running in total..." % (self.comm.rank, self.comm.size))
        self.comm.Barrier() # wait for everybody to synchronize _here_

    def broadcast_cores(self):
        """ broadcast using many cores"""
        pprint.pprint("-"*78)
        pprint.pprint(" Running on %d cores" % self.comm.size)
        pprint.pprint("-"*78)

        self.comm.Barrier()
        # Prepare a vector of N=5 elements to be broadcasted...
        N = 5
        if self.comm.rank == 0:
            A = numpy.arange(N, dtype=numpy.float64)    # rank 0 has proper data
        else:
            A = numpy.empty(N, dtype=numpy.float64)     # all other just an empty array

        # Broadcast A from rank 0 to everybody
        self.comm.Bcast( [A, MPI.DOUBLE] )

        # Everybody should now have the same...
        print("[%02d] %s" % (self.comm.rank, A))

    def scatter_gatter(self):
        """scatter gatter """

        pprint.pprint("-"*78)
        pprint.pprint(" Running on %d cores" % self.comm.size)
        pprint.pprint("-"*78)

        my_N = 4
        N = my_N * self.comm.size

        if self.comm.rank == 0:
            A = numpy.arange(N, dtype=numpy.float64)
        else:
            A = numpy.empty(N, dtype=numpy.float64)

        my_A = numpy.empty(my_N, dtype=numpy.float64)

        # Scatter data into my_A arrays
        self.comm.Scatter( [A, MPI.DOUBLE], [my_A, MPI.DOUBLE] )

        pprint.pprint("After Scatter:")
        for r in range(self.comm.size):
            if self.comm.rank == r:
                print("[%d] %s" % (self.comm.rank, my_A))
            self.comm.Barrier()

        # Everybody is multiplying by 2
        my_A *= 2

        # Allgather data into A again
        self.comm.Allgather( [my_A, MPI.DOUBLE], [A, MPI.DOUBLE] )

        pprint.pprint("After Allgather:")
        for r in range(self.comm.size):
            if self.comm.rank == r:
                print("[%d] %s" % (self.comm.rank, A))
            self.comm.Barrier()

    def benchmarck(
        self,
        BENCHMARH = "MPI Bandwidth Test",
        skip = 10,
        loop = 100,
        window_size = 64,
        skip_large = 2,
        loop_large = 20,
        window_size_large = 64,
        large_message_size = 8192,
        MAX_MSG_SIZE = 1<<27,
        ):

        comm = MPI.COMM_WORLD
        myid = comm.Get_rank()
        numprocs = comm.Get_size()
        print(numprocs)

        if numprocs != 2:
            if myid == 0:
                errmsg = "This test requires exactly two processes"
            else:
                errmsg = None
            raise SystemExit(errmsg)

        s_buf = self.allocate(MAX_MSG_SIZE)
        r_buf = self.allocate(MAX_MSG_SIZE)

        if myid == 0:
            print ('# %s' % (BENCHMARH,))
        if myid == 0:
            print ('# %-8s%20s' % ("Size [B]", "Bandwidth [MB/s]"))

        #message_sizes = [2**i for i in range(30)]
        message_sizes = [2**i for i in range(15)]
        for size in message_sizes:
            if size > MAX_MSG_SIZE:
                break
            if size > large_message_size:
                skip = skip_large
                loop = loop_large
                window_size = window_size_large

            iterations = list(range(loop+skip))
            window_sizes = list(range(window_size))
            requests = [MPI.REQUEST_NULL] * window_size
            #
            comm.Barrier()
            if myid == 0:
                s_msg = [s_buf, size, MPI.BYTE]
                r_msg = [r_buf,    4, MPI.BYTE]
                for i in iterations:
                    if i == skip:
                        t_start = MPI.Wtime()
                    for j in window_sizes:
                        requests[j] = comm.Isend(s_msg, 1, 100)
                    MPI.Request.Waitall(requests)
                    comm.Recv(r_msg, 1, 101)
                t_end = MPI.Wtime()
            elif myid == 1:
                s_msg = [s_buf,    4, MPI.BYTE]
                r_msg = [r_buf, size, MPI.BYTE]
                for i in iterations:
                    for j in window_sizes:
                        requests[j] = comm.Irecv(r_msg, 0, 100)
                    MPI.Request.Waitall(requests)
                    comm.Send(s_msg, 0, 101)
            #
            if myid == 0:
                MB = size / 1e6 * loop * window_size
                s = t_end - t_start
                print ('%-10d%20.2f' % (size, MB/s))

    def allocate(self, n):
        try:
            return mmap.mmap(-1, n)
        except (ImportError, EnvironmentError):
            try:
                from numpy import zeros
                return zeros(n, 'B')
            except ImportError:
                from array import array
                return array('B', [0]) * n

if __name__ == "__main__":
    instance = MPI4PY_EVALUATION()
    #instance.hello_world()
    #instance.scatter_gatter()
    instance.benchmarck()

