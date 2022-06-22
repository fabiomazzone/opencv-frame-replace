def make_is_in_generator(generator):
    gen = generator()
    cur = next(gen)

    def is_prime(n):
        nonlocal cur
        while(cur <= n):
            if(n == cur):
                return True
            else:
                cur = next(gen)
        return False

    return is_prime    
