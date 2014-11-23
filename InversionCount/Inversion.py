input = [1,20,6,4,5]
output = [0] * len(input)

def getInversionCount(input, start, end) :
    if (start < end) :
        mid = (start + end) / 2
        leftInversion = getInversionCount(input, start, mid)
        rightInversion = getInversionCount(input, mid + 1, end)
        mergeInversion = getMergeInversion(input, start, mid, end)
        return leftInversion + rightInversion + mergeInversion
    else :
        return 0
        

def getMergeInversion(input , start, mid, end) :
    mergeInversion = 0
    i = start
    j = mid + 1
    for k in range(start,end + 1) :
        if i != mid + 1 and j != end + 1 :
            if input[i] < input[j] :
                output[k] = input[i]
                i = i + 1
            else :
                mergeInversion = mergeInversion + mid - i + 1
                output[k] = input[j]
                j = j + 1
        else :
            if i == mid + 1:
                for m in range(j,end + 1) :
                    output[k] = input[m]
                    k = k + 1
            else :
                for m in range(i,mid + 1) :
                    output[k] = input[m]
                    k = k + 1
                    
            break
        
    #This loop is to copy the output elements to input
    #At each breakup this is required as input has to be updated as it is used in merge of next bigger parts
    for k in range(start,end + 1) : 
        input[k] = output[k]
        
    return mergeInversion





if __name__ == "__main__" : 
    print getInversionCount(input, 0, len(input) - 1)