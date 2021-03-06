'''
1
3 3 2
1 2
2 3
3 1

1
4 5 3
1 2
2 4
3 4
1 4
1 3
'''
from __builtin__ import True

def isValid(adj,color,index,currColor):
    
    for i in adj[index]:
        if color[i] != -1 and color[i] == currColor:
            return False
    return True
    

def dfs(adj,color,Q,source):
    
    if source == len(adj):
        return True
    
    for c in xrange(Q):
        
        color[source] = c
        valid = isValid(adj, color, source, c)
        print color,source,valid
        if valid:
            res = dfs(adj,color,Q,source + 1)
            if res:
                return True
            else:
                color[source] = -1
        else:
            color[source] = -1
    
    return False
    

    

    
for _ in xrange(input()):
    N,M,Q = map(int,raw_input().split())
    
    adj = [[] * N for _ in xrange(N)]
    
    for _ in xrange(M):
        a,b = map(int,raw_input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
        
    color = [-1] * N
    #print isValid(adj, [0,1,1,2], 2, 1)
    
    result = dfs(adj,color,Q,0)
    if result:
        print True
    else:
        print False
    
    
        
    
    
    
    
    