
def getIdFromDict(h, a, c):
    if h.get(a) is None:
        h[a] = c[0]
        c[0] += 1
    
    return h[a]


        
    
        





def dfs(li, N, source, visited, color, toAssignColor):
    visited[source] = True
    color[source] = toAssignColor
    nextVertexColor = not toAssignColor
    for nextVertex in xrange(N):
        if li[source][nextVertex]:
            if not visited[nextVertex]:
                possible = dfs(li, N, nextVertex, visited, color, nextVertexColor)
                if not possible:
                    return False
            else:
                if color[nextVertex] != nextVertexColor:
                    return False
    return True


def checkBipartite(li, N):
    
    visited = [False] * N
    color = [None] * N
    
    for i in xrange(N):
        if not visited[i]:
            possible = dfs(li, N, i, visited, color, True)
            if not possible:
                return False
    return True
    


if __name__ == '__main__':
    for t in xrange(input()):
        M = input()
        h = {}
        c = [0]
        li = [[None] * 200 for i in xrange(200)]
        for i in xrange(M):
            a, b = raw_input().split()
            ha = getIdFromDict(h, a, c)
            hb = getIdFromDict(h, b, c)
            li[ha][hb] = li[hb][ha] = True
            
        result = checkBipartite(li, c[0])
        result = "Yes" if result else "No"
        out = "Case #" + str(t + 1) + ": " + str(result)
        print out
            
    
    
