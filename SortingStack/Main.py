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
        
    def printStack(self):
        print self.inp
        
    def sortStack(self):
        sort = Stack([])
        while not self.isEmpty():
            item = self.pop()
            sort.insertItem(item)
            #print sort.printStack()
            
        return sort
    
    def top(self):
        return self.inp[-1]        
            
            
    def insertItem(self,item):
        if self.isEmpty():
            self.push(item)
        elif self.top() > item:
            self.push(item)
        else:
            item1 = self.pop()
            self.insertItem(item)
            self.push(item1) 
            
            
        
if __name__ == '__main__':
    s1 = Stack([5,4,1,6,2])
    s1.printStack()
    s1.sortStack().printStack()
    s1.printStack()