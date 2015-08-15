from collections import deque
class Stack:
    def __init__(self,inp):
        self.q1 = deque()
        self.q2 = deque()
        if inp is not None:
            for i in inp:
                self.q1.append(i)
                
    def push(self,item):
        self.q1.append(item)
        
    def pop(self):
        item = None
        if len(self.q1) > 0 :
            while len(self.q1) != 1:
                item = self.q1.popleft()
                self.q2.append(item)
            item = self.q1.popleft()
            self.q1,self.q2 = self.q2,self.q1
            return item
        else:
            return None
        
    def printStack(self):
        for i in self.q1:
            print i,
        print

if __name__ == '__main__':
    s = Stack([1,2,3,4,5])
    print s.pop()
    s.printStack()
    s.push(6)
    s.printStack() 
    print s.pop()   
    s.printStack()     