# URL : https://www.hackerrank.com/challenges/dijkstrashortreach
from heapq import heappush, heappop


def dijkstra(al, source):
    dist = [-1] * len(al)
    dist[source] = 0
    heap = []
    for d, w in al[source]:
        heappush(heap, (w, d))
    num = 1
    while num != len(al):
        while len(heap) and dist[heap[0][1]] >= 0:
            heappop(heap)
        if len(heap):
            w, d = heappop(heap)
            dist[d] = w
            num += 1
            for d1, w1 in al[d]:
                if dist[d1] < 0:
                    heappush(heap, (dist[d] + w1, d1))
        else:
            break
                
    return dist
            
for _ in xrange(input()):
    N, M = map(int, raw_input().split())
    # edges = [(1, 2, 24), (1, 4, 20), (3, 1, 3), (4, 3, 12)]
    al = [[] for i in xrange(N)]
    for _ in xrange(M):
        s, d, w = map(int, raw_input().split())
        al[s - 1].append((d - 1, w))
        al[d - 1].append((s - 1, w))
    
    # print al    
    source = input() - 1
    
        
    s = dijkstra(al, source)
    for i in s:
        if i != 0:
            print i,
    print
