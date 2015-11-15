class QuickFind:
    def __init__(self, li):
        self.p = range(len(li))
        
    def find(self, a):
        '''
        Time Complexity is O(1)
        '''
        if a < 0 or a > len(self.p):
            return None
        else:
            return self.p[a]
        
    def union(self, a, b):
        '''
        Time Complexity is O(N)
        '''
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.p[a] = pb
            for i, v in enumerate(self.p):
                if v == pa:
                    self.p[i] = pb
                    
                    
    


def runTestCase(inp, li):  
    q = QuickFind(li)
    for i, j in inp:
        q.union(i, j)
        print q.p
          
                    
if __name__ == '__main__':
    li = range(10)
    inp = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]
    runTestCase(inp, li)
