mod = 10 ** 9 + 7
import sys
sys.setrecursionlimit(10000)

def combination(n,r):
    num = 1
    denom = 1
    
    for i in xrange(1 , min(n-r,r) + 1):
        num = num * n
        n -= 1
        denom = denom * i

    return num // denom
        

    
a = input()
b = input()

if a < b:
    a,b = b,a
    

   
result = 0
if a == 25 and b < 24:
    result = combination(a + b - 1,b) % mod
elif b >= 24 and (a - b) == 2:
    result = (pow(2,a-26,mod) * (combination(48,24) % mod)) % mod
    
print result
    
    