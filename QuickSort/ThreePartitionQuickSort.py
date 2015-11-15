def quickSort(inp):
    quickSortUtil(inp, 0, len(inp) - 1)
    
def quickSortUtil(inp, low, high):
    if low < high:
        lt, hi = partition(inp, low, high)
        quickSortUtil(inp, low, lt)
        quickSortUtil(inp, hi, high)
        
def partition(inp, low, high):
    pivot = inp[low]
    lt = eq = gt = low + 1
    for i in xrange(low + 1, high + 1):
        if inp[i] < pivot:
            inp[lt], inp[eq], inp[gt] = inp[gt], inp[lt], inp[eq]
            lt += 1
            eq += 1
            gt += 1
        elif inp[i] == pivot:
            inp[eq], inp[gt] = inp[gt], inp[eq]
            eq += 1
            gt += 1
        else:
            gt += 1
    
    inp[low], inp[lt-1] = inp[lt-1], inp[low]
    return lt - 1, eq
            
if __name__ == '__main__':
    inp = [8, 5, 7, 8, 15, 13, 8, 7]
    quickSort(inp)
    print inp
