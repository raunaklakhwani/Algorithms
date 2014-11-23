import numpy

input = [1,2,3,4,5,6,7,8,-9,-8,-7,-6,-5,43,32,23,21]
output = [0] * len(input)
#output = numpy.zeros(len(input))

def mergeSort(input, start, end) :
    if(start < end) :
        mid = (start + end) / 2
        mergeSort(input, start, mid)
        mergeSort(input, mid+1, end)
        merge(input, start, mid, end)

def merge(input, start, mid, end):
    i = start
    j = mid + 1
    for k in range(start,end + 1) :
        if i != mid + 1 and j != end + 1 :
            if input[i] < input[j] :
                output[k] = input[i]
                i = i + 1
            else :
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
                


if __name__ == "__main__":
    mergeSort(input, 0, len(input) - 1)
    print input