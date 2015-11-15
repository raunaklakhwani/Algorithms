from pprint import pprint
from heapq import heappush, heappop

timeInADay = 24    

   
def getResult(final, adj, mat, time, end, heap, source):
    final = [[False for i in xrange(N)] for t in xrange(timeInADay)]
    newtime = time
    newsource = source
    for nextvertex in adj[newsource]:
        if mat[newtime][newsource][nextvertex] != float("inf"):
            heappush(heap, (mat[newtime][newsource][nextvertex], mat[newtime][newsource][nextvertex] % timeInADay, nextvertex, newsource, newtime))
    while len(heap):
        #print heap[0]
        total, hour, nextSource, oldsource, oldtime = heappop(heap)
        final[oldtime][oldsource] = True
        if nextSource == end:
            return total
        else:
            newtime = hour
            newsource = nextSource
            for nextvertex in adj[newsource]:
                if mat[newtime][newsource][nextvertex] != float("inf") and not final[newtime][newsource]:
                    heappush(heap, (total + mat[newtime][newsource][nextvertex], (total + mat[newtime][newsource][nextvertex]) % timeInADay, nextvertex, newsource,newtime))
            
            
    return float("inf")

if __name__ == '__main__':
    for test in xrange(input()):
        N, M, K = map(int, raw_input().split())
        adj = [[] for i in xrange(N)]
        
        mat = [[[float("inf") if i != j else 0 for i in xrange(N)] for j in xrange(N)] for t in xrange(timeInADay)]
        final = [[[-1 for i in xrange(N)] for j in xrange(N)] for t in xrange(timeInADay)]
        
        for i in xrange(M):
            a, b = map(int, raw_input().split())
            c = map(int, raw_input().split())
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
            
            for j in xrange(len(c)):
                mat[j][a - 1][b - 1] = c[j]
                mat[j][b - 1][a - 1] = c[j]
                
        
        res = ""        
        for i in xrange(K):
            D, S = map(int, raw_input().split())
            if test == 8 and i == 29:
                print i
            ans = getResult(final, adj, mat, S, D - 1, [], 0)
            res += str(ans) if ans != float("inf") else "-1"
            res += " "
            
        
            
            
            
                
        
       
        
        
            
                    
                    
                
                
        
        
        
        out = "Case #" + str(test + 1) + ": " + str(res.strip())
        print out
