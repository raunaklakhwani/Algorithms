#URL : http://www.geeksforgeeks.org/prop-tiger-interview-experience/
def check(h,c):
    for key in h:
        if h[key] != c[key]:
            return False
    return True
    

from collections import defaultdict

s = "123456342184321"
p = "1234"
s = "1234432131342"
s = "4325124322233421"

ans = 0
h = defaultdict(int)
for i in p:
    h[i] += 1

c = defaultdict(int)
flag = False
start = None
l = 0
for i,j in enumerate(s):
    if h[j]:
        if start is None:
            start = i
            c[j] += 1
            l += 1
        else:
            c[j] += 1
            
            if c[j] > h[j]:
                if j == s[start]:
                    c[j] -= 1
                    start += 1
                else:
                    flag = False
                    start = None
                    del c
                    c = defaultdict(int)
                    l = 0
            else: 
                l += 1
                    
            
        if  l == len(p):
            if check(h,c):
                ans += 1
            flag = False
            start = None
            del c
            c = defaultdict(int)
            l = 0
        
            
    else:
        flag = False
        start = None
        del c
        c = defaultdict(int)
        l = 0
        
print ans
        
        
            
        
    