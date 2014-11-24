#Video link for proof : https://www.youtube.com/watch?v=T3T7T8Ym20M
import copy # For doint the deep copy of the list use copy.deepcopy(list)
import math
import sys  # For getting the max value of int use sys.maxint

input = [(1,2),(3,4),(4,5),(1,3),(2,6),(7,8),(2,5)]

def bruteForceClosestPair() :
    minSource=''
    minDestination=''
    minDistance = sys.maxint
    length = len(input)
    for i,source in enumerate(input) :
        for j in range(i + 1,length) :
            destination = input[j]
            distance = calculateDistance(source, destination)
            if(distance < minDistance) :
                minSource = source
                minDestination = destination
                minDistance = distance
           
    closestPairList = [minSource,minDestination,minDistance]     
    return closestPairList
                
            
            
            
            
            
            

def calculateDistance(source,destination) :
    distance = math.sqrt(pow(destination[0] - source[0], 2) + pow(destination[1] - source[1], 2))
    return distance



if __name__ == "__main__":
    print bruteForceClosestPair()