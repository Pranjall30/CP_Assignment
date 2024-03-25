def print_primes(N):
    primes = []
    i = 2
    while len(primes) < N:
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)
            if len(primes) == N:
                break
        i += 1
    print(primes[::2])

print_primes(5)