# URL : http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
li = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
def swap(li, a, b):
    li[a], li[b] = li[b], li[a]
    
def partition(inp, low, high):
    print
    i = 0
    lt = 0
    while i <= high:
        if inp[i] == 0:
            swap(inp,lt,i)
            lt += 1
            i += 1
        elif inp[i] == 1:
            i += 1 
        else:
            swap(inp,i,high)
            high -= 1
        
        

        
partition(li, 0, len(li) - 1)
print li
    
    
