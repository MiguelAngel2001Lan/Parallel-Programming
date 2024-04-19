from mpi4py import MPI
import math
import sys
import time
import csv

def f(x):
    return math.sqrt(1 - x**2)

def compute_pi_mpi(N, process_rank, num_processes):
    delta_x = 1.0 / N
    local_sum = 0.0
    for i in range(process_rank, N, num_processes):
        x_i = (i + 0.5) * delta_x
        local_sum += f(x_i) * delta_x
    return local_sum

if __name__ == '__main__':
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000
    start_time = MPI.Wtime()
    local_pi = compute_pi_mpi(N, MPI.COMM_WORLD.Get_rank(), MPI.COMM_WORLD.Get_size())
    global_sum = MPI.COMM_WORLD.reduce(local_pi, op=MPI.SUM, root=0)
    end_time = MPI.Wtime()

    if MPI.COMM_WORLD.Get_rank() == 0:
        pi_estimate = global_sum * 4
        computation_time = end_time - start_time
        with open('mpi_performance.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([N, computation_time])
