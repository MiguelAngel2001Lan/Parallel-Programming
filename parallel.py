from multiprocessing import Pool
import math

def f(x):
    return math.sqrt(1 - x**2)

def partial_sum(start_end):
    start, end, delta_x = start_end
    partial_sum_value = 0
    for i in range(start, end):
        x_i = i * delta_x
        partial_sum_value += f(x_i) * delta_x
    return partial_sum_value

def compute_pi_parallel(N, processes):
    delta_x = 1.0 / N
    pool = Pool(processes)
    intervals = [(i * N // processes, (i + 1) * N // processes, delta_x) for i in range(processes)]
    partial_sums = pool.map(partial_sum, intervals)
    pool.close()
    pool.join()
    return sum(partial_sums) * 4

# This block ensures that the code that follows will only be executed if the script is run directly,
# not if it is imported as a module.
if __name__ == '__main__':
    N = 1000000  # Number of rectangles
    processes = 4  # Number of processes
    approx_pi = compute_pi_parallel(N, processes)
    print(f"Approximated value of pi using multiprocessing: {approx_pi}")
