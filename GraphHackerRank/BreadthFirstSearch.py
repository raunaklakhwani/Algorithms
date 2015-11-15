# URL : https://www.hackerrank.com/challenges/bfsshortreach
from _collections import deque


def bfs(al, source):
    q = deque([source, None])
    visited = [False] * len(al)
    calcLength = [-1] * len(al)
    visited[source] = True
    count = 0
    while len(q):
        item = q.popleft()
        if item is not None:
            calcLength[item] = count
            for next in al[item]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        else:
            count += 1
            if len(q):
                q.append(None)
            else:
                break
        
        
    return calcLength

for _ in xrange(input()):
    N, M = map(int,raw_input().split())
    #edges = [(1, 2), (1, 3)]
    al = [[] for i in xrange(N)]
    for i in xrange(M):
        s,d = map(int,raw_input().split())
        al[s - 1].append(d - 1)
        al[d - 1].append(s - 1)
    
    #print al    
    source = input()
    c = bfs(al,source - 1)
    
    for i in c:
        if i != 0:
            print i if i < 0 else i * 6,
    print