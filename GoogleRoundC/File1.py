'''
5
3 1000
1000
0 0
0 1
0 3
3 1000
1000
1 0
1 1
1 2
5 1000
500 200 1000
0 0
0 1
1 0
3 2
1 1
5 1000
500 2500 1000
0 0
0 1
1 0
3 2
1 1
5 1000
500 2200 1000
0 0
0 1
1 0
3 2
1 1
'''
#from pprint import pprint
import resource
def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


for _ in xrange(input()):
    N, d = map(int, raw_input().split())
    a = [0] + map(int, raw_input().split()) + [0]
    
    coords = []
    #graph = [[0] * N for i in xrange(N)]
    dp = [[float("inf")] * N for _ in xrange(N)]
    for i in xrange(N):
        x, y = map(int, raw_input().split())
        j = len(coords) - 1
        while j >= 0:
            x1, y1 = coords[j]
            dist = manhattan(x, y, x1, y1)
            dp[i][j] = max(dist * d - a[i],0)
            dp[j][i] = max(dist * d - a[j],0)
            #graph[i][j] = dist
            #graph[j][i] = dist
            j = j - 1
        coords.append((x, y))
        
    #del coords
        
    #pprint(graph) 
    
    
    #===========================================================================
    # for i in xrange(N):
    #     for j in xrange(N):
    #         dp[i][j] = max(graph[i][j] * d - a[i],0)
    #         
    #===========================================================================
    #pprint(dp)
    
    #del graph
    
    for k in xrange(1,N - 1):
        for i in xrange(N):
            if k != i:
                for j in xrange(N):
                    if k != j and i != j:
                        #m = max(0, dp[i][k] + dp[k][j] - a[k] - a[i] - a[j])
                        m = dp[i][k] + dp[k][j]
                        dp[i][j] = min(dp[i][j], m)
                
                
    #pprint(dp)
    print dp[0][N-1],
    print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000
    
    
    
    
