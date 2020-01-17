def factorization(n, prime=[], i=2):
    if n > i:
        if n % i == 0:
            prime.append(i)
            return factorization(n / i, prime, i)
        else:
            return factorization(n, prime, i + 1)
    else:
        prime.append(int(n))
        return prime


print(factorization(18))