def fibonacci_sequence():
    n_2, n_1 = 0, 1

    while(True):
        yield n_2

        n_2, n_1 = n_1, n_1 + n_2


def prime_sequence():
    primes = list()
    n = 2
    while(True):
        is_prime = True
        for p in primes:
            if(n % p == 0):
                is_prime = False
                break

        if(is_prime):
            primes.append(n)
            yield n
        
        n += 1