import sys
import math
import copy

#input = [1, 2, -1, 3, 6, 7, 9, 8]
input = [2,2,2,2,2]
K = 4

def bruteForceMethod() :
    '''
    Time Complexity is O(n^2)
    '''
    length = len(input)
    for i,indexElement in enumerate(input) : 
        for j in range(i + 1, length) :
            if indexElement + input[j] == K : 
                return [indexElement,input[j]]
    return "No Such Element Found"

def smartMethod() :
    '''
    Time complexity is O(nlogn) due to sorting of elements
    '''
    input1 = copy.deepcopy(input)
    input1.sort()
    length = len(input)
    start = 0
    end = length - 1
    while start < end : 
        if input1[start] + input1[end] == K :
            return [input1[start],input1[end]]
        elif input1[start] + input1[end] < K : 
            start = start + 1
        else :
            end = end - 1
    return "No Such Element Found" 


        

if __name__ == '__main__':
    print bruteForceMethod()
    print smartMethod()
