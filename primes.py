def primes(n):
    s = set(range(2, n))
    for m in range(2, n//2):
        for k in range(2*m, n, m):
            if k in s:
                s.remove(k)
    return s

if __name__ == '__main__':
    print('primes(100) =')
    print(primes(100))
    print('')
    print('len(primes(100000)) = ')
    print(len(primes(100000)))
