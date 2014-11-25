import sys
import math
import copy

input = [1, 2, -1, 3, 6, 7, 9, 8]
K = 20

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

if __name__ == '__main__':
    print bruteForceMethod()
