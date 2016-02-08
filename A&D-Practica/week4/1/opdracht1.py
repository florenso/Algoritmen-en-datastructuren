class ChainingHashDemo:
     def __init__(self):
         self.len = 0
         self.table = [None]*self.len
         self.hashTableSet = set()

     def search(self, e):
        return self.hashTableSet.__contains__(e)

     def insert(self,e):
         if not self.search(e):
             self.len += 1
             self.hashTableSet.add(e)
             return True
         else:
             return False

     def delete(self, e):
         if self.search(e):
             self.len -= 1
             self.hashTableSet.remove(e)
             return True
         else:
             return False

     def __repr__(self):
         output_string = ""
         for value in self.hashTableSet:
             output_string += "[key = " + str(value) + "]\n"
         output_string += "len = " + str(self.len)
         return output_string

     def rehash(self, newLen):
        #todo
        return True

chd = ChainingHashDemo()

chd.insert(8)
chd.insert(2)
chd.insert(4)
chd.insert(9)

print(chd)
