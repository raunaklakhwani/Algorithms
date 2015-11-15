from math import sqrt
numBikers, numBikes, K = 3, 3, 2
bikers = [(0, 1), (0, 2), (0, 3)]
bikes = [(100, 1), (200, 2), (300, 3)]

li = [[0] * numBikes for i in xrange(numBikers)]
calculateDistance = lambda x, y : round(sqrt((y[1] - x[1]) ** 2 + (y[0] - x[0]) ** 2), 2)

for i in xrange(numBikers):
    for j in xrange(numBikes):
        li[i][j] = calculateDistance(bikers[i], bikes[j])
        
#print li



def bfs(distance, bikers, bikes, numBikers, numBikes, time, visitedBikes, bikesAssigned, biker):
    for i in xrange(numBikes):
        if not visitedBikes[i] and distance[biker][i] <= time:
            visitedBikes[i] = True
            if bikesAssigned[i] < 0:
                bikesAssigned[i] = biker
                return True
            else:
                currentBikerOnBike = bikesAssigned[i]
                isPossible = bfs(distance, bikers, bikes, numBikers, numBikes, time, visitedBikes, bikesAssigned, currentBikerOnBike)
                if isPossible:
                    bikesAssigned[i] = biker
                    return True
    return False
                    
                
            
            
        


def maxNumberOfBikersMappingInGivenTime(distance, bikers, bikes, numBikers, numBikes, time):
    bikesAssigned = [-1] * numBikes
    for biker in xrange(numBikers):
        visitedBikes = [False] * numBikes
        isPossible = bfs(distance, bikers, bikes, numBikers, numBikes, time, visitedBikes, bikesAssigned, biker)
        if isPossible:
            if sum([1 for i in bikesAssigned if i >= 0]) >= K:
                return True
            
    return False


lo = 0
hi = 10 ** 7

while lo < hi:
    mid = (lo + hi) / 2
    isPossible = maxNumberOfBikersMappingInGivenTime(li, bikers, bikes, numBikers, numBikes, mid)
    if isPossible:
        hi = mid
    else:
        lo = mid + 1
        
print lo
