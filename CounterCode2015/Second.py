'''
2 3
1 5
1 5 5
NYY
YYN
'''
from heapq import heappop, heappush
p, b = map(int, raw_input().split())
s = map(int, raw_input().split())
q = map(int, raw_input().split())

graph = [[0] * b for _ in xrange(p)]
for i in xrange(p):
    s1 = raw_input()
    for j in xrange(b):
        graph[i][j] = (1 if s1[j] == "Y" else 0)

ansc = 0
ans = 0
miniansc = 0
minans = float("inf")

def bfs(graph, person, visited, assignedBikes):
    
    heap = []
    
    for bike in xrange(len(graph[person])):
        heappush(heap, (-1 * q[bike], graph[person][bike],bike))
    while len(heap):
        a,interestedBike,bike = heappop(heap)
        if interestedBike and not visited[bike]:
            visited[bike] = True
            # Checking if bike was freely available
            if assignedBikes[bike] < 0:
                assignedBikes[bike] = person
                return True
            else:
                candidateOnThisJob = assignedBikes[bike]
                isPossible = bfs(graph, candidateOnThisJob, visited, assignedBikes)
                if isPossible:
                    assignedBikes[bike] = person
                    return True
            
    return False  


def maxMatch(graph):
    global ans,ansc
    result = 0
    p = len(graph)
    b = len(graph[0])
    assignedBikes = [-1] * b
    for person in xrange(p):
        visited = [False] * b
        isPossible = bfs(graph, person, visited, assignedBikes)
        temp = 0
        count = 0
        for i in xrange(b):
            if assignedBikes[i] != -1:
                count += 1
                temp += (s[assignedBikes[i]] * q[i])
        #print count
        #=======================================================================
        # if ansc < count:
        #     ans = temp
        #     ansc = count
        #=======================================================================
        
            
            
        if ans < temp and count == p:
            ans = max(temp,ans)
        #print assignedBikes
        if isPossible:
            result += 1
    return result


def minbfs(graph, person, visited, assignedBikes):
    
    heap = []
    
    for bike in xrange(len(graph[person])):
        heappush(heap, (q[bike], graph[person][bike],bike))
    while len(heap):
        a,interestedBike,bike = heappop(heap)
        if interestedBike and not visited[bike]:
            visited[bike] = True
            # Checking if bike was freely available
            if assignedBikes[bike] < 0:
                assignedBikes[bike] = person
                return True
            else:
                candidateOnThisJob = assignedBikes[bike]
                isPossible = minbfs(graph, candidateOnThisJob, visited, assignedBikes)
                if isPossible:
                    assignedBikes[bike] = person
                    return True
            
    return False  


def minMatch(graph):
    global minans,miniansc
    result = 0
    p = len(graph)
    b = len(graph[0])
    assignedBikes = [-1] * b
    for person in xrange(p):
        visited = [False] * b
        isPossible = minbfs(graph, person, visited, assignedBikes)
        temp = 0
        count = 0
        for i in xrange(b):
            if assignedBikes[i] != -1:
                temp += (s[assignedBikes[i]] * q[i])
                count += 1
        
        #=======================================================================
        # if miniansc < count:
        #     minans = temp
        #     miniansc = count
        #=======================================================================
            
        
        if minans > temp and count == p:
            minans = min(temp,minans)
        #print assignedBikes
        if isPossible:
            result += 1
    return result

        
#print graph
maxMatch(graph)
minMatch(graph)


#print ans
print minans,ans
