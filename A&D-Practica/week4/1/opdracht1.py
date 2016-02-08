import math

class ChainingHashDemo:
    def __init__(self):
        self.len = 7
        self.hashTableSet = [None]*self.len
        itera = 0
        for dummy in self.hashTableSet:
            self.hashTableSet[itera] = set()
            itera += 1

    def search(self, searchValue):
        for subset in self.hashTableSet:
            for e in subset:
               if(searchValue == e):
                   return True
        return False

    def isTherePlaceForUs(self):
        itera = 0
        currentFillingDegree = 0
        for value in self.hashTableSet:
            currentFillingDegree += len(set(value))
            if (currentFillingDegree / self.len) > 0.75:
                return False
        return True

    def insert(self,e):
        hashTemp = hash(e) % self.len

        if not self.search(e):
            if not self.isTherePlaceForUs():
                self.rehash(self.len * 2) #rehasing table two times the size.

            valuesInSet = set( self.hashTableSet[ hashTemp] )
            valuesInSet.add(e)
            self.hashTableSet[ hashTemp] = valuesInSet

            return True
        else:
            return False

    def delete(self, e):
        if self.search(e):
            itera = 0
            for theSet in self.hashTableSet:
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
        itera = 0
        for value in self.hashTableSet:
            output_string += "["+ str(itera) +" = " + str(value) + "]\n"
            itera += 1
        output_string += "len = " + str(self.len)
        return output_string

    def rehash(self, newLen):
        tempList = [None]*newLen
        itera = 0
        for dummy in tempList:
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

chd.insert(8.3) #
chd.insert(8.3)

#chd.delete(8.3)

chd.insert(4.3) #
chd.insert(2.23) #
chd.insert(4.12) #
chd.insert(12.34) #

#chd.delete(12.34)

chd.insert(32.34) #
chd.insert(13.34) #
chd.insert(56.34) #
chd.insert(5.34)#
chd.insert(5.34)
chd.insert(45)
chd.insert(23)
#chd.insert(90)
#chd.insert(190)
print(chd)

