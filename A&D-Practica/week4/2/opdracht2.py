import random

def sameHash():
    num = random.random()
    hashNum= hash( num )
    dict = {hashNum: num}

    while True:
        num = random.random()
        hashNum = hash( num )
        if hashNum in dict:
            print('hash(', dict.get( hashNum ), ') == hash(', num, ') == ', hashNum )
            return {dict.get( hashNum ),num}
            break
        else:
            dict[hashNum] = num
            if len(dict)>1000000:
                print('te lang')
                break;

print(sameHash())