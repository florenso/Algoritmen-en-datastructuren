def fac(n):
     totalValue = 1
     for number in range(n, 1, -1):
        totalValue *= number
     return totalValue

def B(n,k):
    cFac = fac(n - k)
    nFac = fac(n)
    kFac = fac(k)
    return nFac // kFac // cFac


print("Faculteit van 9: " + str(fac(9)))
print("Resultaat van B(100,50): " + str(B(100,50)))

