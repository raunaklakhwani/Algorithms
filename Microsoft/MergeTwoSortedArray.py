# URL : http://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/

A = [2, 8, None, None, None, 13, None, 15, 20]
B = [5, 7, 9, 25]


def shiftLeft(li):
    p = 0
    for i in xrange(len(li)):
        if li[i] is not None:
            li[i],li[p] = li[p],li[i]
            p += 1
        
    return li,p-1


def merge(A,B,m):
    h1 = m
    h2 = len(B) - 1
    p = len(A) - 1
    
    while h1 >= 0 and h2 >= 0:
        if A[h1] > B[h2]:
            A[p] = A[h1]
            h1 -= 1
        else:
            A[p] = B[h2]
            h2 -= 1
        p -= 1
    
    while h1 >= 0:
        A[p] = A[h1]
        h1 -= 1
        
    while h2 >= 0:
        A[p] = B[h2]
        h2 -= 1
        
    return A



A,m = shiftLeft(A)
print A,m

print merge(A,B,m)


