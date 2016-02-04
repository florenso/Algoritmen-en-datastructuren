import sys

sys.setrecursionlimit(1000000000)

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random


count = 0
wcs = False

def rqsort(a,low,high):
    global count
    global wcs
    count =  count + 1
    if low < high:

        if wcs:
            pivot = a[low:high].index(min(a[low:high]))+low

            #print(low,high,pivot)
            #print (a[pivot])
            #print(a[low:high])
        else:
            pivot = random.randint(low,high)


        swap(a,low, pivot) # plaats pivot op positie low
        m = low
        for j in range(low+1,high+1):
            count =  count + 1
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
                                # low < i <= m : a[i] < a[low]
                                # i > m : a[i] >= a[low]
        swap(a,low,m)
                                # low <= i < m : a[i] < a[m]
                                # i > m : a[i] >= a[m]
        rqsort(a,low,m-1)
        rqsort(a,m+1,high)

def qsort(a):
    global count
    count = 0
    rqsort(a,0,len(a)-1)

testList = []

a = 0
while a < 10000:
    a += 1
    testList.append( random.randint( 0, 1000000 ) )

testlist1=list(testList)
#print( testList )

print('normal test')
qsort( testList )
print(count)
#print( testList )


print('worst case test')
wcs=True
qsort( testlist1 )
print(count)
#print( testlist1 )