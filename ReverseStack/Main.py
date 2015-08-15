class Stack:
    def __init__(self,inp):
        self.inp = []
        if inp is not None:
            for i in inp:
                self.push(i)
                
    def push(self,item):
        self.inp.append(item)
        
    def pop(self):
        return self.inp.pop()
    
    def isEmpty(self):
        return len(self.inp) == 0
    
    def reverseStack(self):
        if not self.isEmpty():
            item = self.pop()
            self.reverseStack()
            self.insertAtBottom(item)
        else:
            return
            
    def insertAtBottom(self,item):
        if not self.isEmpty():
            item1 = self.pop()
            self.insertAtBottom(item)
            self.push(item1)
        else:
            self.push(item)
        
    def printStack(self):
        print self.inp
        
if __name__ == '__main__':
    s1 = Stack([1,2,3,4,5])
    s1.printStack()
    s1.reverseStack()
    s1.printStack()