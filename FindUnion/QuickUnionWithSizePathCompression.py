class QuickUnionWithSizePathCompression:
    '''
    The idea is to store the parent node of each node in p except for the root. roots parent is set to the (-1 * size of the tree).
    So when doing union, we see the size of the trees and set the lower tree as a child of the bigger tree.
    And In the Find operation, search for the node till the root and the node that came in the between, set their parent to the root.
    
    In theory, this is not linear but in practice this is actually linear
    Any operation of Munion and Find operation on N objects will take O(N + Mlg*N) time where lg*N is the number of log operations
    to be done for a number to reach 1
    '''
    def __init__(self, li):
        self.p = [-1] * len(li)
        
    def find(self, a):
        '''
        Time Complexity is O(depth)
        '''
        if a < 0 or a > len(self.p):
            return None
        else:
            
            if self.p[a] < 0:
                return (a, self.p[a])
            else:
                # a = self.p[a]
                m, n = self.find(self.p[a])
                self.p[a] = m
                return (m, n)
        
    def union(self, a, b):
        '''
        Time Complexity is O(depth)
        '''
        pa, sa = self.find(a)
        pb, sb = self.find(b)
        if pa != pb:
            if sa < sb:
                self.p[pb] = pa
                self.p[pa] += sb
            else:
                self.p[pa] = pb
                self.p[pb] += sa
            

def runTestCase(inp, li):  
    q = QuickUnionWithSizePathCompression(li)
    for i, j in inp:
        q.union(i, j)
        print (i, j), q.p
          
                    
if __name__ == '__main__':
    li = range(10)
    inp = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (5, 8), (6, 1)]
    runTestCase(inp, li)
