import time
from multiprocessing import Pool, cpu_count

def calculate_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize_parallel(number):
    with Pool(cpu_count()) as pool:
        factors_list = pool.map(calculate_factors, number)

    return factors_list

def main():
    numbers = [128, 255, 99999, 10651060]

    # Parallel version
    start_time_parallel = time.time()
    result_parallel = factorize_parallel(numbers)
    end_time_parallel = time.time()

    print("Parallel Execution Time:", end_time_parallel - start_time_parallel)
    print("Result (Parallel):", result_parallel)

if __name__ == "__main__":
    main()
