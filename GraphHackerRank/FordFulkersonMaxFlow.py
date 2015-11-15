# URL : https://www.hackerrank.com/challenges/kruskalmstrsub
from _collections import defaultdict, deque

def bfs(al, source, sink):
    visited = [False] * len(al)
    parent = [0] * len(al)
    visited[source] = True
    parent[source] = -1
    breakFlag = False
    q = deque([source])
    while len(q):
        item = q.popleft()
        for d in al[item]:
            if not visited[d] and al[item][d] > 0:
                q.append(d)
                visited[d] = True
                parent[d] = item
                if d == sink:
                    breakFlag = True
                    break
        
        if breakFlag:
            break
    if breakFlag:   
        return True, parent
    else:
        return False, parent

def getMaxFlow(al, source, sink):
    maxFlow = 0
    while True:
        isPath, parent = bfs(al, source, sink)
        if isPath:
            temp = sink
            minimum = float("inf")
            while parent[temp] != -1:
                v = temp
                u = parent[temp]
                minimum = min(minimum, al[u][v])
                temp = u
                
            temp = sink
            while parent[temp] != -1:
                v = temp
                u = parent[temp]
                al[u][v] -= minimum
                al[v][u] += minimum
                temp = u
                
            maxFlow += minimum
        else:
            break
    return maxFlow

                    
N, M = 4, 6
edges = [(1, 2, 3), (2, 3, 4), (3, 1, 2), (2, 2, 5), (3, 4, 3), (4, 3, 3)]

al = [defaultdict(int) for _ in xrange(N)]
for s, d, w in edges:
    if s != d:
        al[s - 1][d - 1] += w
        al[d - 1][s - 1] += w
    
print al
print getMaxFlow(al, 0, N - 1)
    

    

    
    
    


