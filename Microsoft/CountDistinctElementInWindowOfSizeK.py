# URL : http://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/
from collections import defaultdict
li = [1, 2, 1, 3, 4, 2, 3]
k = 4

m = defaultdict(int)
t = 0
for i in xrange(k):
    m[li[i]] += 1
    if m[li[i]] == 1:
        t += 1
    

for i in xrange(k,len(li)):
    print t
    m[li[i]] += 1
    if m[li[i]] == 1:
        t += 1
    
    m[li[i-k]] -= 1
    if m[li[i-k]] == 0:
        t -= 1
        
print t
    
    
    


    