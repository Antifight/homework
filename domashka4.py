import time


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if primes[start]:
            for multiple in range(start * start, limit + 1, start):
                primes[multiple] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


def benchmark(limit):
    start = time.time()
    sieve_of_eratosthenes(limit)
    sieve_time = time.time() - start

    print(f"Limit: {limit}")
    print(f"Sieve method time: {sieve_time:.6f} sec")
    print("-" * 30)


for limit in [100, 1000, 10000]:
    benchmark(limit)