# Video link for proof : https://www.youtube.com/watch?v=T3T7T8Ym20M
import copy  # For doint the deep copy of the list use copy.deepcopy(list)
import math
import sys  # For getting the max value of int use sys.maxint

#input = [(1,2),(2,3),(1,3),(4,3),(2,2)]
#input = [(1, 2), (3, 4), (4, 5), (1, 3), (2, 6), (7, 8), (2, 5)]
input = [(1,2),(1,4),(2,4)]

output = {"source" : "" , "destination" : "" , "minDistance" : ""}

# Time complexity is O(n^2)
def bruteForceClosestPair() :
    minSource = ''
    minDestination = ''
    minDistance = sys.maxint
    length = len(input)
    for i, source in enumerate(input) :
        for j in range(i + 1, length) :
            destination = input[j]
            distance = calculateDistance(source, destination)
            if(distance < minDistance) :
                minSource = source
                minDestination = destination
                minDistance = distance
           
    closestPairList = [minSource, minDestination, minDistance]     
    return closestPairList




# Time Complexity id O(nlogn)                
def divideAndConquerClosestPair() :
    inputX = copy.deepcopy(input)
    inputX.sort(key=lambda point : point[0])   
    findClosestPair(inputX, 0, len(inputX) - 1)
    return output

def findClosestPair(inputX, start, end) :
    if start == end : 
        return None
    elif start + 1 == end :
        distance = calculateDistance(inputX[0], inputX[1])
        #Saving the output 
        if distance < output["minDistance"] :
            output["minDistance"] = distance
            output["source"] = inputX[0]
            output["destination"] = inputX[1]
        return distance
    else :
        mid = (start + end) / 2
        leftMinDistance = findClosestPair(inputX, start, mid)
        rightMinDistance = findClosestPair(inputX, mid + 1, end)
        if leftMinDistance is not None and rightMinDistance is not None : 
            minDistance = min(leftMinDistance,rightMinDistance)
        elif leftMinDistance is None :
            minDistance = rightMinDistance
        else :
            minDistance = leftMinDistance
        minSplitDistance = splitClosestPair(inputX, start, mid, end, minDistance)
        if minSplitDistance is None : 
            return minDistance
        else :
            return minSplitDistance
        
def splitClosestPair(inputX, start, mid, end, minDistance):
    minSplitDistance = None
    inputY = []
    left = inputX[mid][0] - minDistance
    right = inputX[mid][0] + minDistance
    for i in range(start, end + 1) :
        point = inputX[i]
        if point[0] >= left and point[0] <= right :
            inputY.append(point)
    
    inputY.sort(key = lambda point : point[1])
    
    length = len(inputY)
    for i,source in enumerate(inputY) :
        end = i+8
        if length < end :
            end = length
        for j in range(i+1,end) :
            destination = inputY[j]
            distance = calculateDistance(source, destination)
            if (minSplitDistance is None and distance < minDistance) or (minSplitDistance is not None and distance < minSplitDistance) :
                minSplitDistance = distance
                output["minDistance"] = distance
                output["source"] = source
                output["destination"] = destination
    return minSplitDistance        
            
            
            

def calculateDistance(source, destination) :
    distance = math.sqrt(pow(destination[0] - source[0], 2) + pow(destination[1] - source[1], 2))
    return distance



if __name__ == "__main__":
    print bruteForceClosestPair()
    print divideAndConquerClosestPair()
