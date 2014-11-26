import copy

input = [1, 2, 4, 3, 1, 33, 5, 6, 7]

def firstSmartMethod() :
    '''
    Time Complexity : O(nlogn due to sorting)
    ''' 
    input1 = copy.deepcopy(input)
    input1.sort()
    
    for index,element in enumerate(input1) :
        if element == input1[index+1] :
            return element
    
    return "No Duplicate Element"
    
def secondSmartMethod() :
    '''
    Used dictionary to save values
    Time Complexity : O(n)
    Space Complexity : O(n)
    '''
    dict = {}
    for index,element in enumerate(input) :
        if dict.get(element) is None :
            dict[element] = True
        else :
            return element

    return "No Duplicate Element"
    
if __name__ == '__main__':
    print firstSmartMethod()
    print secondSmartMethod()