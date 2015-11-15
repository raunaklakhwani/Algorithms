from fractions import gcd
from bisect import bisect_left, bisect_right

def getResult(lnp, lne, lnt, p, q):
    g = gcd(p, q)
    p = p / g
    q = q / g
    
    for i in xrange(len(lnp)):
        for j in xrange(len(lnt)):
            for k in xrange(len(lne)):
                for l in xrange(len(lne)):
                    if k != l:
                        a = lnp[i]
                        b = lne[k]
                        c = lne[l]
                        d = lnt[j]
                        
                        a = a * c
                        b = b * d
                        
                        g1 = gcd(a, b) 
                        a /= g1
                        b /= g1
                        
                        #=======================================================
                        # g1 = gcd(lnp[i], lne[k])
                        # a /= g1
                        # b /= g1
                        # 
                        # g2 = gcd(lne[l], lnt[j])
                        # c /= g2
                        # d /= g2
                        # 
                        # left = a * c
                        # right = b * d
                        #=======================================================
                        left = (float)(a) / b
                        right = (float)(p) / q
                        if abs(left - right) <= 1e-6:
                            return True
    return False
        
    
def getResult1(lnp, lne, lnt, p, q):
    g = gcd(p, q)
    p = p / g
    q = q / g
    
    l1 = []
    l2 = []
    for i in xrange(len(lnp)):
        for j in xrange(len(lne)):
            res = lnp[i] * lne[j]
            if res % p == 0:
                l1.append((i,j))
                
    for i in xrange(len(lne)):
        for j in xrange(len(lnt)):
            res = lne[i] * lnt[j]
            if res % q == 0:
                l2.append((i,j))
                
    for i1,j1 in l1:
        for i2,j2 in l2:
            if j1 != i2:
                num = lnp[i1] * lne[j1]
                denom = lne[i2] * lnt[j2]
                g = gcd(num,denom)
                num /= g
                denom /= g
                
                if num == p and denom == q:
                    return True
                
    
    return False
    

if __name__ == '__main__':
    for test in xrange(input()):
        raw_input()
        np, ne, nt = map(int, raw_input().split())
        lnp = map(int, raw_input().split())
        lne = map(int, raw_input().split())
        lnt = map(int, raw_input().split())
        
        # lnp.sort()
        # lne.sort()
        # lnt.sort()
        
        M = input()
        out = "Case #" + str(test + 1) + ":"
        print out
        for _ in xrange(M):
            p, q = map(int, raw_input().split())
            print "Yes" if getResult1(lnp, lne, lnt, p, q) else "No"
            
            
        
        
        #=======================================================================
        # M = input()
        # p, q = map(int, raw_input().split())
        # 
        # for i, v1 in enumerate(lnp):
        #     for j, v2 in enumerate(lnt):
        #         g = gcd(p * v2, q * v1)
        #         m = (p * v2) / g
        #         n = (q * v1) / g
        #         if m > n:
        #             for k in xrange(len(lne) - 1):
        #                 v3 = lne[k]
        #                 x = bisect_left(lne, v3 * ((float)(m) / n), k + 1, len(lne))
        #                 if x == 
        #                 
        #                 
        #             
        #         elif m < n:
        #             print 
        #         else:
        #             x = bisect_left(lne, m)
        #             if lne[x] == m and (x + 1) < len(lne) and lne[x + 1] == m:
        #                 print "Yes" 
        #             else:
        #                 print "No"
        #=======================================================================
                    
        
        
        
                
                
            
        
