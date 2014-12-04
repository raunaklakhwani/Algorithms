import random
input = [2, 4, 1, 3, 5,-1,13,13]

def swap(indexA, indexB) :
    '''
    Swaps the two integers
    '''
    input[indexA], input[indexB] = input[indexB], input[indexA]

def partition(pivotIndex, start, end) :
    '''
    Partitions the array around pivot.
    Logic is bring the pivot to the start first
    Then do a linear scan to find the index where the pivot is to be replaced.
    The idea is to have two variables i and j
    i points to the start of the second array i.e elements greater than the pivot
    Run Time of partition is O(n)
    Note if u replace < than sign with > than it will do decreasing order
    '''
    if pivotIndex != start :
        swap(pivotIndex, start)
    pivot = input[start]
    i = start + 1
    for j in range(start + 1, end + 1) :
        if input[j] > pivot :
            swap(i, j)
            i = i + 1
    
    swap(i - 1, start)
    return i - 1

def quickSort(start, end) :
    '''
    Randomized Quick Sort algorithm
    Time Complexity is O(n log n)
    Constant Space
    For complexity : https://class.coursera.org/algo-004/lecture
    Complexity calculation very important
    '''
    if start < end :
       pivotIndex = random.randint(start, end)
       p = partition(pivotIndex, start, end)
       quickSort(start, p - 1)
       quickSort(p + 1, end) 
            

if __name__ == '__main__':
    quickSort(0, len(input) - 1)
    print input
