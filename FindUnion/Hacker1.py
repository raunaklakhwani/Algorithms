# URL :https://www.hackerrank.com/challenges/components-in-graph
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
                
    def getMinMaxComponent(self):
        
        minimum = float("inf")
        maximum = float("-inf")
        for i in self.p:
            if i < 0 and i != -1:
                if minimum > abs(i):
                    minimum = abs(i)
                if maximum < abs(i):
                    maximum = abs(i)
                    
        return (minimum, maximum)
            
                
    
if __name__ == '__main__':
    N = input()
    #li = [(1, 6), (2, 7), (3, 8), (4, 9), (2, 6)]
    q = FindUnion(2 * N)
    for i in xrange(N):
        a,b = map(int,raw_input().split())
        q.union(a - 1, b - 1)
        print (a - 1, b - 1), list(enumerate(q.p))
        
    minimum, maximum =  q.getMinMaxComponent()
    print minimum,maximum
    
                
            
        
            
