m=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
max = 10000
import random

matrix={}#maakt een dict aan en word gebruikt als een matrix
for i  in range(0,len(m)):
    matrix[i,0]=1
for j in range(0,max+1):
    matrix[0,j]=1

for i in range(1,len(m)):
    for j in range(1,max+1):
        if j >= m[i]:
            matrix[i,j]=matrix[i-1,j]+matrix[i,j-m[i]]
        else:
            matrix[i,j]=matrix[i-1,j]


def f(cent):
    return matrix[len(m)-1,cent]


for i in range(0,20):
    if i <5:
        num=random.randint(1,10)
    elif i < 10:
        num=random.randint(1,100)
    else:
        num=random.randint(1,max)
    euro,cent= divmod(num,100)
    print('je kan €', euro, 'en', cent, 'cent op', f( num ), 'verschillende manieren betalen' )


