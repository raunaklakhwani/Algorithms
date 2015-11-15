# URL : http://www.geeksforgeeks.org/sort-array-according-order-defined-another-array/
inp = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
inp1 = [2, 1, 8, 3]

#===============================================================================
# inp = [2, 3, 7, 10, 12]
# inp1 = [1, 5, 7, 8]
# 
# inp = [10, 12]
# inp1 = [5, 7, 9]
#===============================================================================

def quickSort(inp, cmp=None):
    quickSortUtil(inp, 0, len(inp) - 1, cmp)
    
def quickSortUtil(inp, low, high, cmp=None):
    if low < high:
        lt, hi = partition(inp, low, high, cmp)
        quickSortUtil(inp, low, lt - 1, cmp)
        quickSortUtil(inp, hi, high, cmp)
        
def partition(inp, low, high, cmp=None):
    if cmp is None:
        pivot = inp[low]
        lt = eq = gt = low + 1
        for i in xrange(low + 1, high + 1):
            if inp[i] < pivot:
                if lt != eq and lt != gt and gt != eq:
                    inp[lt], inp[eq], inp[gt] = inp[gt], inp[lt], inp[eq]
                elif lt == eq:
                    inp[lt], inp[gt] = inp[gt], inp[lt]
                elif lt == gt:
                    inp[lt], inp[eq] = inp[eq], inp[lt]
                elif eq == gt:
                    inp[lt], inp[gt] = inp[gt], inp[lt]
                lt += 1
                eq += 1
                gt += 1
            elif inp[i] == pivot:
                inp[eq], inp[gt] = inp[gt], inp[eq]
                eq += 1
                gt += 1
            else:
                gt += 1
        
        inp[low], inp[lt - 1] = inp[lt - 1], inp[low]
        return lt - 1, eq
    else:
        pivot = inp[low]
        lt = eq = gt = low + 1
        for i in xrange(low + 1, high + 1):
            compare = cmp(inp[i], pivot) 
            if compare < 0:
                if lt != eq and lt != gt and gt != eq:
                    inp[lt], inp[eq], inp[gt] = inp[gt], inp[lt], inp[eq]
                elif lt == eq:
                    inp[lt], inp[gt] = inp[gt], inp[lt]
                elif lt == gt:
                    inp[lt], inp[eq] = inp[eq], inp[lt]
                elif eq == gt:
                    inp[lt], inp[gt] = inp[gt], inp[lt]
                lt += 1
                eq += 1
                gt += 1
            elif compare == 0:
                inp[eq], inp[gt] = inp[gt], inp[eq]
                eq += 1
                gt += 1
            else:
                gt += 1
        
        inp[low], inp[lt - 1] = inp[lt - 1], inp[low]
        return lt - 1, eq
        
        

h = {}
for i in xrange(len(inp1)):
    h[inp1[i]] = i

def myCompare(a, b):
    ha = h.get(a, float("inf"))
    hb = h.get(b, float("inf"))
    if ha == hb:
        return 0
    elif ha > hb:
        return 1
    else:
        return -1
    

quickSort(inp, myCompare)

print inp
        
    
    
    

        
