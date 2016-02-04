class ListNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        if self.tail != None:
            current = self.tail.next
            s= s + str(current)         #prints head
            if self.tail != current:    #checks if there is more then one item in list
                current = current.next
                while current != self.tail.next:    #print loop for items in list
                    s = s + " -> " + str(current)
                    current=current.next
        else:
            s= 'empty list'
        return s

    def addLast(self,e):
        if self.tail == None:
            self.tail = ListNode(e,self.tail)
            self.tail.next=self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = n


    def delete(self,e):
        if self.tail == None:
            print('cant delete, empty list')
        elif self.tail == self.tail.next:
            if e == self.tail.data:
                print('deleted:',e)
                del self.tail
                self.tail = None
            else:
                print(e,'not found, cant delete')
        else:
            current = self.tail
            while current.next != self.tail:
                if current.next.data == e:
                    tmp = current.next
                    current.next= current.next.next
                    del tmp
                    print('deleted:',e)
                current=current.next



mylist =  MyLinkedList()
print(mylist)
mylist.addLast(1)
mylist.addLast(2)
mylist.addLast(3)
mylist.addLast(4)
mylist.addLast(5)
mylist.addLast(6)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(1)
print(mylist)
mylist.delete(3)
print(mylist)
mylist.delete(4)
print(mylist)
mylist.delete(5)
mylist.delete(5)
print(mylist)
mylist.delete(6)
print(mylist)
mylist.delete(5)
