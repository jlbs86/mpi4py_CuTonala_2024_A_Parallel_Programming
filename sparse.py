import numpy as np
from mpi4py import MPI
import scipy as sp

def parallel_sparse_matrix_vector_multiplication(rows, cols, values, vector):
  comm = MPI.COMM_WORLD
  size = comm.Get_size()
  print("tama:",size)
  rank = comm.Get_rank()

  # Determine the number of rows each process will handle
  rows_per_process = len(rows) // size

  # Determine the start and end indices for each process
  start_index = rank * rows_per_process
  end_index = start_index + rows_per_process if rank != size - 1 else len(rows)

  # Each process calculates its part of the result vector
  local_result = np.zeros(len(vector))
  for i in range(start_index, end_index):
      local_result[rows[i]] += values[i] * vector[cols[i]]

  # Gather the results from all processes
  result = np.zeros(len(vector))
  comm.Reduce(local_result, result, op=MPI.SUM, root=0)

  if rank == 0:
    return result

if __name__ == "__main__":
  num_values = 10000
  rng = np.random.default_rng()
  rvs = sp.stats.poisson(25, loc=10).rvs
  S = sp.sparse.random_array((num_values, num_values), density=0.25, random_state=rng, data_sampler=rvs)

  
  indices = S.coords
  values = S.data

  rows = np.array(indices[0])
  cols = np.array(indices[1])
  values = np.array(values)
  vector = np.random.randint(low=1, high=10, size=num_values)
  # Example sparse matrix in COO format
  # This is a 4x4 matrix with 5 non-zero elements
  #rows = np.array([0, 0, 1, 2, 2, 3])
  #cols = np.array([0, 2, 2, 0, 3, 3])
  #values = np.array([1, 2, 3, 4, 5, 6])

  # Example vector
  #vector = np.array([1, 2, 3, 4])
  print("Result:", parallel_sparse_matrix_vector_multiplication(rows, cols, values, vector))