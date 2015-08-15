import sys
class Stack:
    def __init__(self,inp):
        self.inp = []
        self.top = -1
        self.dummy = [sys.maxint]
        if inp is not None:
            for i in inp:
                self.push(i)
                
    def push(self,item):
        self.inp.append(item)
        self.top += 1
        if item < self.dummy[-1]:
            self.dummy.append(item)
        
    def pop(self):
        if self.top == -1:
            print "No item found"
            return None
        else:
            self.top -= 1
            item = self.inp.pop()
            if item == self.dummy[-1]:
                self.dummy.pop()
                
            return item
        
    def getMinimum(self):
        return self.dummy[-1]
        
        
if __name__ == '__main__':
    inp = [1,5,0,2,9,3,-1,-2,-1]
    s1 = Stack([])
    s2 = Stack(inp)
    
    for i in xrange(len(inp)):
        print s2.pop()
        print s2.inp
        print s2.getMinimum()
        print "______________________"
            
    
            