import random

num = random.random()
hashNum= hash( num )
dict = {hashNum: num}

while True:
    num = random.random()
    hashNum = hash( num )
    if hashNum in dict:
        print('hash(', dict.get( hashNum ), ') == hash(', num, ') == ', hashNum )
        break
    else:
        print('loop')
        dict[hashNum] = num
