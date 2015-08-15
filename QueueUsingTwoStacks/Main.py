class Queue:
    def __init__(self, inp):
        self.s1 = []
        self.s2 = []
        if inp is not None:
            for i in inp:
                self.s1.append(i)
    
    def enqueue(self, item):
        self.s1.append(item)
        
    def dequeue(self):
        if len(self.s2) != 0:
            return self.s2.pop()
        else:
            if len(self.s1) != 0:
                while len(self.s1) != 0:
                    self.s2.append(self.s1.pop())
                return self.s2.pop()
            else:
                return None
            
            
    def printQueue(self):
        for i in xrange(len(self.s2) -1,-1,-1):
            print self.s2[i],
        for i in xrange(len(self.s1)):
            print self.s1[i],
        print
        
if __name__ == '__main__':
    q = Queue([1,2,3,4,5])
    print q.dequeue()
    q.enqueue(6)
    q.printQueue()
            
