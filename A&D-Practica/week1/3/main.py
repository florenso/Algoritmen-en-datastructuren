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
    for i in prm:
        if prm[i]:
            print(i)
            count+=1
    return count

#print(primes_sieve1(1000))
print('in totaal zijn er ',find_primes(1000),' priem getallen')




