import sys
import math
import copy

input = [1, 2, -1, 3, 6, 7, 9, 8]
# input = [2,2,2,2,2]
K = 4

def bruteForceMethod() :
    '''
    Time Complexity is O(n^3)
    '''
    length = len(input)
    for i, indexElement in enumerate(input) : 
        for j in range(i + 1, length) :
            for k in range(j + 1, length) :
                if indexElement + input[j] + input[k] == K : 
                    return [indexElement, input[j], input[k]]
    return "No Such Element Found"

def smartMethod() :
    '''
    Time complexity is O(n^3)
    '''
    input1 = copy.deepcopy(input)
    input1.sort()
    length = len(input)
    
    for index, element in enumerate(input1) :
        start = index + 1
        end = length - 1
        while start < end : 
            if element + input1[start] + input1[end] == K :
                return [element, input1[start], input1[end]]
            elif element + input1[start] + input1[end] < K : 
                start = start + 1
            else :
                end = end - 1
    return "No Such Element Found" 

def secondSmartMethod() :
    '''
    Time Complexity : O(n^2)
    Space Complexity : O(n)
    Logic : For each element(key), save the pair of the elements with the remaining sum.
    '''
    input1 = copy.deepcopy(input)
    input1.sort() 
    length = len(input1)
    dict = {}
    for index,element in enumerate(input1) :
        start = 0
        end = length - 1
        if start == index : 
            start = start + 1
        if end == index : 
            end = end - 1
        sum = K - element
        while start < end : 
            if input1[start] + input1[end] == sum :
                list = dict.get(element,[])
                list.append((input1[start],input1[end]))
                dict[element] = list
                start = start + 1
                end = end - 1
                if start == index : 
                    start = start + 1
                if end == index : 
                    end = end - 1
            elif input1[start] + input1[end] > sum : 
                end = end - 1
                if end == index : 
                    end = end - 1
            else :
                start = start + 1
                if start == index : 
                    start = start + 1
    
    print dict 
    output = []               
    for index,element in enumerate(input1) :
        list =  dict.get(element)
        if list is not None :
            for pair in list :
                output.append((element,pair[0],pair[1]))
        
    if len(output) == 0 :
        return "No Such Element Found"
    else :
        return output
             
                        
        
        

if __name__ == '__main__':
    print bruteForceMethod()
    print smartMethod()
    print secondSmartMethod()
    
