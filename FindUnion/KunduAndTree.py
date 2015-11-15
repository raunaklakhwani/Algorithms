# URL :https://www.hackerrank.com/challenges/kundu-and-tree
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
                
            
                
    
if __name__ == '__main__':
    mod = 10 ** 9 + 7
    N = input()
    #li = [(1, 2, 'b'), (2, 3, 'r'), (3, 4, 'r'), (4, 5, 'b')]
    q = FindUnion(N)
    for i in xrange(N - 1):
        a, b, c = raw_input().split()
        if c == 'b':
            a = int(a)
            b = int(b)
            q.union(a - 1, b - 1)
            #print (a - 1, b - 1), list(enumerate(q.p))
            
    
    m = [-1 * i for i in q.p if i < 0]
    
    
    
    dp = [[0] * 4 for i in xrange(len(m) + 1)]
    for i in xrange(1,len(m) + 1):
        dp[i][1] = dp[i-1][1] + m[i - 1]
            
    for i in xrange(2,4):
        for j in xrange(1,len(m) + 1):
            dp[j][i] = (dp[j-1][i] + m[j-1] * dp[j-1][i-1]) % mod

    print dp[len(m)][3]