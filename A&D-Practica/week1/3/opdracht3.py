def find_primes(limit):
    lmt = limit +1
    prm = dict()
    for i in range(2,lmt):
        prm[i]=True

    for i in prm:
        factors = range(i, lmt, i)
        for i2 in factors[1:]:
            prm[i2] = False

    count = 0
    all_primes = []
    for i in prm:
        if prm[i]:
            all_primes.append(i)
            count+=1
    return all_primes

#print(primes_sieve1(1000))
print('Dit zijn de priemgetallen onder 1000: ',find_primes(1000))




