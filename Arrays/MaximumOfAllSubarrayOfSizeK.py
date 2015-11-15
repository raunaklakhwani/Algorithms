# URL : http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
from collections import deque
#inp = [1, 2, 3, 1, 4, 5, 2, 3, 6]
#inp = [3, 2, 1, 1, 4, 5, 2, 3, 6]
inp = [2, 3, 1, 1, 4, 5, 2, 3, 6]
k = 3

def printMaxInAWindow(inp, k):
    q = deque([])
    for i in xrange(k):
        while len(q) and inp[i] >= inp[q[-1]]:
            q.pop()
        q.appendleft(i)
        #print q
        
    for i in xrange(k,len(inp)):
        print inp[q[-1]],
        while len(q) and ((i - q[-1]) == k or inp[i] >= inp[q[-1]]):
            q.pop()
            
        while len(q) and ((i - q[0]) == k or inp[i] >= inp[q[0]]):
            q.popleft()
        
        q.appendleft(i)
        #print q
    
    print inp[q[-1]]
        
        
        
            
        
        
        
   
                    
                
                
                
        
        # print q
        
        
        
        
        
        
    

if __name__ == '__main__':
    printMaxInAWindow(inp, k)
