#pop's and pushes on -1
#keep that in mind for peeking!
class myStack( list):

    def push(self,x):
        self.append(x)

    def peek(self,num):
        return self[num]

    def isEmpty(self):
        if len(self) is 0:
            return True
        return False



test = myStack()
print('empty? ',test.isEmpty())
test.push(10)
test.push(50)
print('empty? ',test.isEmpty())
test.push(51)
test.push(52)
test.push(53)
test.push(54)
test.push(55)
print(test.pop())
print(test.pop())
print('peeking at 4',test.peek(4))
