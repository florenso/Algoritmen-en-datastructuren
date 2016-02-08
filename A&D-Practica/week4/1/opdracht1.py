import math
import random

class ChainingHashDemo:
    def __init__(self):
        self.len = 7
        self.hashTableSet = [None]*self.len
        for itera, dummy in enumerate(self.hashTableSet):
            self.hashTableSet[itera] = set()
            itera += 1

    def search(self, searchValue):
        for subset in self.hashTableSet:
            for e in subset:
               if(searchValue == e):
                   return True
        return False

    def countFillingDegree(self):
        currentFillingDegree = 0
        for itera, value in enumerate(self.hashTableSet):
            currentFillingDegree += len(set(value))
            if (currentFillingDegree / self.len) > 0.75:
                return False
        return True

    def insert(self,e):
        hashTemp = hash(e) % self.len

        if not self.search(e):
            if not self.countFillingDegree():
                self.rehash(self.len * 2) #rehasing table two times the size.

            valuesInSet = set( self.hashTableSet[ hashTemp] )
            valuesInSet.add(e)
            self.hashTableSet[ hashTemp] = valuesInSet

            return True
        else:
            return False

    def delete(self, e):
        if self.search(e):
            for itera, theSet in enumerate(self.hashTableSet):
                if set(theSet).__contains__(e):
                    currentSet = set(theSet)
                    currentSet.remove(e)
                    self.hashTableSet[ itera ] = currentSet
                    return True
                itera += 1
        else:
            return False

    def __repr__(self):
        output_string = "\n====HASHING TABLE====\n"
        for itera, value in enumerate(self.hashTableSet):
            output_string += "["+ str(itera) +" = " + str(value) + "]\n"
            itera += 1
        output_string += "\nlen = " + str(self.len)
        return output_string

    def rehash(self, newLen):
        tempList = [None]*newLen
        for itera, dummy in enumerate(tempList):
            tempList[itera] = set()
            itera += 1

        for subset in self.hashTableSet:
            for e in subset:
                hashTemp = hash(e) % newLen

                valuesInSet = set( tempList[ hashTemp] )
                valuesInSet.add(e)
                tempList[ hashTemp] = valuesInSet

        self.hashTableSet = tempList
        self.len = newLen

chd = ChainingHashDemo()

listOfRandomValues = [random.uniform(1.3,600) for _ in range (200)]



for currentNumber in listOfRandomValues:
    chd.insert(currentNumber)

print("\n=====INSERTED 200 NUMBERS\n")
print(chd)
print("==========================\n")

print("\n=====REMOVED 100 NUMBERS")
for currentNumber in listOfRandomValues[100:]:
    chd.delete(currentNumber)
print(chd)
print("==========================\n")

