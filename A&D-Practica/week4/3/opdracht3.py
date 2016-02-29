def fac(n):
     if n == 1:
          return 1;
     else:
          return n * fac(n - 1)

def B(n,k):
     return((fac(n)//fac(k))//fac(n-k))

print("Faculteit van 9: " + str(fac(9)))
print("Resultaat van B(100,50): " + str(B(100,50)))




