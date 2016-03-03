class myqueue( list):

    def enqueue(self,s):
        self.append(s)

    def dequeue(self):
        return self.pop(0)
