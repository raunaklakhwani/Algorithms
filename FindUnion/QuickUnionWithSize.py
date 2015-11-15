class QuickUnionWithSize:
    '''
    The idea is to store the parent node of each node in p except for the root. roots parent is set to the (-1 * size of the tree).
    So when doing union, we see the size of the trees and set the lower tree as a child of the bigger tree.
    '''
    def __init__(self, li):
        self.p = [-1] * len(li)
        
    def find(self, a):
        '''
        Time Complexity is O(depth)
        Worst Time Complexity is O(log N)
        '''
        if a < 0 or a > len(self.p):
            return None
        else:
            while self.p[a] >= 0:
                a = self.p[a]
            return (a, self.p[a])
        
        
    def union(self, a, b):
        '''
        Time Complexity is O(depth)
        Worst Time Complexity is O(log N)
        This time complexity is due to Find
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
    q = QuickUnionWithSize(li)
    for i, j in inp:
        q.union(i, j)
        print (i, j), q.p
          
                    
if __name__ == '__main__':
    li = range(10)
    inp = [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (5, 9), (7, 3), (4, 8), (6, 1)]
    runTestCase(inp, li)
