import math

def compute_pi(N):
    total_sum = 0
    delta_x = 1.0 / N
    
    for i in range(N):
        x_i = i * delta_x
        f_x_i = math.sqrt(1 - x_i**2)
        total_sum += f_x_i * delta_x
        
    return total_sum * 4

# Example usage:
N = 1000000 # Number of rectangles
approx_pi = compute_pi(N)
print(f"Approximated value of pi: {approx_pi}")
