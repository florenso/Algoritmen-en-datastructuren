def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom \
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal \
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("X",end= " ")
            else:
                print("*",end= " ")
        print()
    print()

def rsearch(N):
    global a
    global t
    for i in range(N):
        if check(a,i):
            a.append(i)
            if len(a) == N:
                print(a)
                #printQueens(a)
                t+=1
                x=a[-1]+1
                del a[-1]
                return False
            else:
                if rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False

a = [] # a geeft voor iedere rij de kolompositie aan
t = 0

rsearch(8)
print('aantal oplossingen:',t)
#print(a)
#printQueens(a)

print('deel 2:')

#===========================================================

from itertools import permutations

n = 8
cols = range(n)
for vec in permutations(cols):
    if n == len(set(vec[i]+i for i in cols)) \
         == len(set(vec[i]-i for i in cols)):
        print (vec )


