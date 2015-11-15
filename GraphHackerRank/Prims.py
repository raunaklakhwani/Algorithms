# URL : https://www.hackerrank.com/challenges/primsmstsub
from heapq import heappush, heappop
class FindUnion:
    def __init__(self, li):
        self.p = [-1] * li
        
    
    def findUtil(self, a):
        if a >= len(self.p) or a < 0:
            return (None, None)
        else:
            if self.p[a] < 0:
                return (a, self.p[a])
            else:
                f = self.findUtil(self.p[a])
                self.p[a] = f[0]
                return (self.p[a], f[1])
            
    def find(self, a):
        if a >= len(self.p) or a < 0:
            return None
        else:
            return self.findUtil(a)[0]
        
    
    def union(self, a, b):
        fa, sa = self.findUtil(a)
        fb, sb = self.findUtil(b)
        
        if fa != fb:
            if sa <= sb:
                self.p[fb] = fa
                self.p[fa] += sb
            else:
                self.p[fa] = fb
                self.p[fb] += sa
                
                
def prims(al, source):
    q = FindUnion(len(al))
    heap = []
    for d, w in al[source]:
        heappush(heap, (w, d, source))
    
    num = 1
    result = 0
    while num != len(al):
        while len(heap) and q.find(heap[0][1]) == q.find(heap[0][2]):
            heappop(heap)
        if len(heap):
            w, d, s = heappop(heap)
            q.union(s, d)
            result += w
            for d1, w1 in al[d]:
                if d1 != s:
                    heappush(heap, (w1, d1, d))
        else:
            break
    return result
    


N, M = map(int,raw_input().split())
#edges = [(1, 2, 3), (1, 3, 4), (4, 2, 6), (5, 2, 2), (2, 3, 5), (3, 5, 7)]
al = [[] for i in xrange(N)]
for _ in xrange(M):
    s,d,w  = map(int,raw_input().split())
    al[s - 1].append((d - 1, w))
    al[d - 1].append((s - 1, w))
    
source = input() - 1
print prims(al, source)
