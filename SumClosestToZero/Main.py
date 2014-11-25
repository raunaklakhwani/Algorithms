
import sys
import math
import copy

# input = [1,3,5,7,-2,-7,-9]
# input = [-1, -2, -3, -4, -5, 5]
input = [1,2,3,4,5,6,7,-9]

def bruteForceSumClosestToZero() :
    '''
    Time Complexity is O(n^2)
    '''
    minSum = sys.maxint
    source = ''
    destination = ''
    
    for i in range(0, len(input)) :
        s = input[i]
        for j in range(i + 1, len(input)) :
            d = input[j]
            if minSum > abs(s + d) :
                minSum = abs(s + d)
                source = s
                destination = d
    return [source, destination, minSum]

def smartClosestToZero() :
    '''
    Time Complexity is O(nlogn) because of sorting
    '''
    input1 = copy.deepcopy(input)
    input1.sort()
    minSum = sys.maxint
    length = len(input1)
    if input1[0] >= 0 :
        source = input1[0]
        destination = input1[1]
        minSum = destination - source
    elif input1[length - 1] <= 0 :
        source = input1[length - 1]
        destination = input1[length - 2]
        minSum = source - destination
    else :
        negIndex = 0;
        posIndex = length - 1
        while negIndex < posIndex and input1[negIndex] < 0 and input1[posIndex] > 0 :
            s = input1[negIndex]
            d = input1[posIndex]
            difference = d + s
            if minSum > abs(difference) : 
                minSum = abs(difference)
                source = s
                destination = d
            if difference < 0  :
                negIndex = negIndex + 1
            elif difference > 0 : 
                posIndex = posIndex - 1
            else :
                negIndex = negIndex + 1
                posIndex = posIndex - 1
              
                
        
    return [source, destination, minSum]
        


if __name__ == '__main__':
    print bruteForceSumClosestToZero()
    print smartClosestToZero()
