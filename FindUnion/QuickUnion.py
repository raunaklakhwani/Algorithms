class QuickUnion:
    def __init__(self, li):
        self.p = range(len(li))
        
    def find(self, a):
        '''
        Time Complexity is O(depth)
        Worst Time Complexity is O(N)
        '''
        if a < 0 or a > len(self.p):
            return None
        else:
            while self.p[a] != a:
                a = self.p[a]
            return a
        
        
    def union(self, a, b):
        '''
        Time Complexity is O(depth)
        Worst Time Complexity is O(N)
        This time complexity is due to Find
        '''
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.p[pa] = pb
            

def runTestCase(inp, li):  
    q = QuickUnion(li)
    for i, j in inp:
        q.union(i, j)
        print (i, j), q.p
          
                    
if __name__ == '__main__':
    li = range(10)
    inp = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]
    runTestCase(inp, li)
