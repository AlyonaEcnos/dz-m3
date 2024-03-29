import time
from multiprocessing import Pool, cpu_count

def calculate_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        factors_list = pool.starmap(calculate_factors, [(num,) for num in numbers])
    return factors_list

def main():
    numbers = [128, 255, 99999, 10651060]

    # Calculate factors directly
    start_time_calculate_factors = time.time()
    factors_calculated = [calculate_factors(num) for num in numbers]
    end_time_calculate_factors = time.time()
    print("Direct Calculation Time:", end_time_calculate_factors - start_time_calculate_factors)

    # Parallel version
    start_time_parallel = time.time()
    result_parallel = factorize_parallel(numbers)
    end_time_parallel = time.time()
    print("Parallel Execution Time:", end_time_parallel - start_time_parallel)

if __name__ == "__main__":
    main()
