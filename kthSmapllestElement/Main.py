import random
input = [21,3,2,4,5,6,7,1,8,9,50]

def swap(indexA,indexB):
    input[indexA],input[indexB] = input[indexB],input[indexA]
    
def partition(pivotIndex,start,end):
    if pivotIndex != start :
        swap(pivotIndex, start)
    
    pivot = input[start]
    i = start + 1
    for j in range(start + 1, end + 1) : 
        if input[j] < pivot :
            swap(i, j)
            i = i + 1
    
    swap(i-1,start)
    return i - 1

def quickSort(start,end):
    if start < end :
        randomPivot = random.randint(start,end)
        p = partition(randomPivot, start, end)
        quickSort(start, p-1)
        quickSort(p+1, end)
        

if __name__ == '__main__':
    print input
    quickSort(0, len(input) - 1)
    print input