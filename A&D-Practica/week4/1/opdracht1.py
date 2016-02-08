import math

class ChainingHashDemo:
    def __init__(self):
        self.len = 7
        self.hashTableSet = [None]*self.len
        itera = 0
        for dummy in self.hashTableSet:
            self.hashTableSet[itera] = set()
            itera += 1


    def search(self, e):
        return self.hashTableSet.__contains__(e)

    def isTherePlaceForUs(self):
        itera = 0
        maxvalue = math.ceil(self.len * 0.25)
        for value in self.hashTableSet:
            if len(set(value)) == 0:
                itera += 1
            if(itera > maxvalue):
                return True
        return False

    def insert(self,e):
        hashTemp = hash(e) % self.len

        if not self.search(hashTemp):
            if not self.isTherePlaceForUs():
                self.rehash(self.len * 2) #rehasing table two times the size.
                print(self)

            valuesInSet = set( self.hashTableSet[ hashTemp] )
            valuesInSet.add(e)
            self.hashTableSet[ hashTemp] = valuesInSet
            return True


        else:
            return False

    def delete(self, e):
        if self.search(e):
            self.hashTableSet.remove(e)
            return True
        else:
            return False

    def __repr__(self):
        output_string = "====HASHING TABLE====\n"
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
chd.insert(4.3) #
chd.insert(2.23) #
chd.insert(4.12) #
chd.insert(12.34) #
chd.insert(32.34) #
chd.insert(13.34) #
chd.insert(56.34) #
chd.insert(5.34)#
chd.insert(5.34)
chd.insert(45)
chd.insert(23)
chd.insert(90)
chd.insert(190)
print(chd)

