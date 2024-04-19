from mpi4py import MPI
import numpy as np
import math

# MPI initialization
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def f(x):
    return math.sqrt(1 - x**2)

def compute_pi_mpi(N, process_rank, num_processes):
    delta_x = 1.0 / N
    local_sum = 0.0
    
    # Split the range of N across all processes
    for i in range(process_rank, N, num_processes):
        x_i = (i + 0.5) * delta_x
        local_sum += f(x_i) * delta_x
    
    return local_sum

if __name__ == '__main__':
    N = 1000000  # Total number of intervals
    local_pi = compute_pi_mpi(N, rank, size)
    
    # Use MPI to reduce all of the local sums into a single sum on the root process
    global_sum = comm.reduce(local_pi, op=MPI.SUM, root=0)
    
    # The root process prints out the final result
    if rank == 0:
        pi_estimate = global_sum * 4
        print(f"Approximated value of pi using mpi4py: {pi_estimate}")
