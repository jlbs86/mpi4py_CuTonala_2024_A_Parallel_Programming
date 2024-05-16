# -*- coding: utf-8 -*-
"""
================================
Evaluate the mpy4py functionality
================================

MPI for Python supports convenient, pickle-based communication
of generic Python object as well as fast, near C-speed,
direct array data communication of buffer-provider objects
(e.g., NumPy arrays).
https://materials.jeremybejarano.com/MPIwithPython/overview.html


Running Python scripts with MPI
Usage:
        $ mpiexec -n 4 python mpi4py_basics.py

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
from mpi4py import MPI
import numpy
import sys


class MPI4PY_UTILS:
    """Utilities for MPI4PY library"""

    def __init__(self) -> None:
        """Then we need to create a communicator, an abstract concept which refers to a world where a predefined number
           of processes can communicate. These processes can arise from processors which are physically at different
           locations connected through a network (typically a cluster). It can also refer to a number of multiple
           processes that can be generated in a single PC or laptop (e.g. 4 core i7 processors can enable spawning
           of 8 processors thanks to hyperthreading). Once a communicator is created, mpi automatically identifies
           them with an number called rank, which starts from 0. Keep in mind that the number of processors is nowhere
           explicitly specified in the code.

           Virtual topologies (Cartcomm, Graphcomm and Distgraphcomm classes, which are specializations of the
           Intracomm class) are fully supported. New instances can be obtained from intracommunicator instances
           with factory methods Intracomm. Create_cart and Intracomm.Create_graph.
        """
        # The two predefined intracommunicator instances are available:
        # COMM_SELF and COMM_WORLD. From them, new communicators can be created as needed.
        self.comm = MPI.COMM_WORLD # create default communicator
        self.rank = self.comm.Get_rank() # Determines the rank of the calling process in the communicator.
        self.size = self.comm.Get_size() # Returns the number of processes in the communicator. 
                                         # It will return the same number to every process.

    def simple_hello_world(self):
        """As tradition has it, we will introduce you to MPI programming using a variation on the standard hello world
           program: your first MPI python program will be the Hello World program for multiple processes.
           The source code is as follows.

           First, the mpiexec program is launched. This is the program which starts MPI, a wrapper around whatever
           program you to pass into it. The -n 5 option specifies the desired number of processes. In our case,
           8 processes are run, each one being an instance of python. To each of the 5 instances of python,
           we pass the argument hello.py which is the name of our program’s text file, located in the current
           directory. Each of the five instances of python then opens the .py file and runs the same program.
           The difference in each process’s execution environment is that the processes are given different ranks
           in the communicator. Because of this, each process prints a different number when it executes.

           Intracommunicators are the most commonly used form of communicator in MPI.
           Each intracommunicator contains a set of processes, each of which is identified by its “rank” within
           the communicator. The ranks are numbered 0 through Size-1. Any process in the communicator can send a
           message to another process within the communicator or receive a message from any other process
           in the communicator. Intracommunicators also support a variety of collective operations that involve
           all of the processes in the communicator. Most MPI communication occurs within intracommunicators.
           Intercommunicators provide a sophisticated method of implementing complex communications,
           but very few MPI programs require them.
           The Hierarchy of Communicators
                    Intercom         
           ----COMM
                    Intracom
                            Cartcomm
                            Distgraphcomm
                            Graphcomm
        """
        # The above command will execute five python processes which can all communicate with each other.
        # When each program runs, it will print hello, and tell you its rank:
        # Example usage and output:
        # (venv) i@is-MacBook-Pro mpi4py_examples % mpirun -np 8 python3 mpi4py_basics.py
        # Hello wolrd from process 5
        # Hello wolrd from process 2
        # Hello wolrd from process 0
        # Hello wolrd from process 4
        # Hello wolrd from process 3
        # Hello wolrd from process 1
        # Hello wolrd from process 7
        # Hello wolrd from process 6
        print(f"Hello wolrd from process {self.rank}")

    def seperate_codes(self):
        """
        When an MPI program is run, each process receives the same code. However, each process is assigned a
           different rank. This allows us to embed a seperate code for each process into one file.
           In the following code, all processes are given the same two numbers. However, though there is only one file,
           3 processes are given completely different instructions for what to do with them.
           Process 0 sums them, process 1 multiplies them, and process 2 takes the maximum of them:
        """
        a = 6.0
        b = 3.0
        if self.rank == 0: # Will be printed if the rank 0 is detected
                print(a + b)
        if self.rank == 1: # Will be printed if the rank 1 is detected
                print(a * b)
        if self.rank == 2: # Will be printed if the rank 2 is detected
                print(max(a,b))

    def pass_random_draw(self):
        """
        As mentioned in earlier, the simplest message passing involves two processes: a sender and a receiver.
        Let us begin by demonstrating a program designed for two processes. One will draw a random number and then
        send it to the other. We will do this using the routines Comm.Send and Comm.Recv:
        """
        rand_num = numpy.zeros(1)
        if self.rank == 1:
            rand_num = numpy.random.random_sample(1)
            print(f"Process {self.rank} drew the number {rand_num[0]}")
            self.comm.Send(rand_num, dest=0)

        if self.rank == 0:
                print(f"Process {self.rank} before receiving has the number {rand_num[0]}")
                self.comm.Recv(rand_num, source=1)
                print(f"Process {self.rank} received the number {rand_num[0]}")

    def send(self, buffer, dest):
        """
        Comm.Send(buf, dest = 0, tag = 0)
        Performs a basic send. This send is a point-to-point communication.
        It sends information from exactly one process to exactly one other process.
        """
        return MPI.COMM_WORLD.Send(buffer, dest)

    def receive(self, buffer, source):
        """
        Comm.Recv(buf, source = 0, tag = 0, Status status = None)¶
        Basic point-to-point receive of data
        Parameters
            Comm (MPI comm): communicator we wish to query
            buf (choice): initial address of receive buffer (choose receipt location)
            source (integer): rank of source
            tag (integer): message tag
            status (Status): status of object
        """
        return MPI.COMM_WORLD.Recv(buffer, source)
    
    def send_and_receive(self):
        """
        Comm.Recv(buf, source = 0, tag = 0, Status status = None)¶
        Basic point-to-point receive of data
        Parameters
            Comm (MPI comm): communicator we wish to query
            buf (choice): initial address of receive buffer (choose receipt location)
            source (integer): rank of source
            tag (integer): message tag
            status (Status): status of object

        Send and Recv are referred to as blocking functions.
        That is, if a process calls Recv, it will sit idle until it has received a message from a corresponding
        Send before it will proceeed. See the appendix for the corresponding non-blocking functions Isend and
        Irecv (I stands for immediate). In essence, Irecv will return immediately.
        If it did not receive its message it will indicate to the system that it will be receiving a message,
        proceed beyond the Irecv to do other useful work, and then check back later to see if the message has arrived.
        This can be used to dramatically improve performance.

        Tip:
        On a Recv you do not always need to specify the source. Instead, you can allow the calling process to accept
        a message from any process that happend to be sending to the receiving process.
        This is done by setting source to a predefined MPI constant, source=ANY_SOURCE
        (note that you would first need to import this with
        from mpi4py.MPI import ANY_SOURCE or use the syntax source=MPI.ANY_SOURCE).
        """
        data_frame = numpy.arange(3)
        if self.rank == 0:
             print(f"Sending data frame: {data_frame}")
             self.send(data_frame, dest=1)
        else:
             print(f"Receiving data frame: {data_frame}")
             self.receive(data_frame, source=0)

    def trap_serial(self, a, b, n):
        """
        Now that we understand basic communication in MPI, we will proceed by parallelizing our first
        algorithm-numerical integration using the “trapezoid rule.”
        Early on in most calculus classes, students learn to estimate integrals using the trapezoid rule.
        A range to be integrated is divided into many vertical slivers, and each sliver is approximated with
        a trapezoid. The area of each trapezoid is computed, and then all their areas are added together.
        https://materials.jeremybejarano.com/MPIwithPython/pointToPoint.html#the-trapezoidal-rule

        python mpi4py_basics.py 0.0 1.0 10000
        """
        integral = (self.support_function(a) + self.support_function(b))/2.0
        x = a
        h = (b-a)/n
        for _ in range(1, int(n)):
              x = x + h
              integral = integral + self.support_function(x)
        return integral * h

    @staticmethod
    def support_function(x):
         """Support method: Assu,e f(x) = xˆ2"""
         return x*x
    
    def trap_parallel_serial(self, a, b, n):
        """The parallel approach to trapezoidal integral estimation starts by dividing the original range among the
        processors. Each process will get a group of one or more trapezoids to calculate area over. Now, notice how
        we decided to implement to division of trapezoids among the processes. The processors individually calculate
        their own ranges to work on. Although this is a small detail, it is fairly important. We could have written
        the algorithm such that process 0 divides up the work for the other processors, then each processor calculates
        its area, and finally a sum is computed. However, this would introduce an unnecessary bottleneck: all
        processes with rank greater than 0 would be waiting for its data range to arrive. By having each process
        calculate its own range, we gain a large speedup.
        Once the integrals are calculated, they are summed up onto process 0.
        Each process with a rank higher than 0 sends it's integral to process 0. The first parameter to the
        Send command is an array storing the information your program wishes to send.
        At the same time, process 0 receives the data from any process. This is what the tag ANY_SOURCE means.
        It tells MPI to not worry about the sender, but rather to just accept data as it comes.
        When Comm.Recv is called, the process must wait for a message to be sent to it.
        If multiple processes are sending a message to the process with Comm.Send, the program will
        call Comm.Recv multiple times - once for each message. The for-loop essentially accomplishes this.
        MPI has two mechanisms specifically designed to partition the message space: tags and communicators.
        The tag parameter is there in the case that two messages with the same size and datatype are
        sent to the same process. In that case, the program would not necessarily be able to tell apart the data.
        So the programmer can attach different tags that he or she defines to the sent data to keep them straight.
        mpiexec -n 4 python mpi4py_basics.py 0.0 1.0 10007
        mpirun -n 4 python mpi4py_basics.py 0.0 1.0 10007
        """
        dest = 0
        total = -1.0
        #h is the step size. n is the total number of trapezoids
        h = (b-a)/n
        #local_n is the number of trapezoids each process will calculate
        #note that size must divide n
        local_n = n/self.size

        #we calculate the interval that each process handles
        #local_a is the starting point and local_b is the endpoint
        local_a = a + self.rank*local_n*h
        local_b = local_a + local_n*h

        #initializing variables. mpi4py requires that we pass numpy objects.
        integral = self.trap_serial(local_a, local_b, local_n)

        # communication
        # root node receives results from all processes and sums them
        if self.rank == 0:
                total = integral
                for source in range(1, self.size):
                        integral = self.comm.recv(source=source)
                        print("PE", self.rank, "<--", source, ",", integral, "\n")
                        total = total + integral
        else:
                # all other process send their result
                print("PE", self.rank, "-->", dest, ",", integral, "\n")
                self.comm.send(integral, dest=0)

        # root process prints results
        if self.comm.rank == 0:
                print("With n =", n, "trapezoids, our estimate of the integral from" , a, "to", b, "is", total)


if __name__ == "__main__":
    instance = MPI4PY_UTILS()
    #instance.simple_hello_world()
    #instance.seperate_codes()
    #instance.pass_random_draw()
    #instance.send_and_receive()
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])

    # Executes with:  python mpi4py_basics.py 0.0 1.0 10000
    #integrtal_1 = instance.trap_serial(a, b, n)
    #if integrtal_1:
    #    print("With n =", n, "trapezoids, our estimate of the integral from", a, "to", b, "is", integrtal_1)

    # Executes with: mpirun -n 4 python mpi4py_basics.py 0.0 1.0 10007
    integral = instance.trap_parallel_serial(a, b, n)
