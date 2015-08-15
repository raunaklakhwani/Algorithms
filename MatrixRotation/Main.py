#URL : https://www.hackerrank.com/challenges/matrix-rotation-algo
def output(li):
    for i in li:
        print " ".join(map(str, i))

def rotateMatrix(li, r):
    # Rotate By 1
    
    rotateMatrixByOne(li, r)

def rotateMatrixByOne(li, r):
    '''
    The idea is to finish the outer layer firsst, then go to secon layer and so on.
    if the rotation value is too large, we can compute the lower rotation value as the layer will become same after certain rotations.
    but the value after which layer becomes same is different for each layer.
    So if r are the total rotations and M,N are the dimensions of layers then r %(M+N-2) are actually the effective rotations as after 
    (M+N-2) rotations, layer will become the same.
    '''
    m = min(M, N) / 2
    for i in xrange(m):
        x = r % (2 * (M + N - 2 - 4 * i))
        for _ in xrange(x):
            srow = scol = i
            endRow = M - i
            endCol = N - i
            
            irow = icol = i
            
            # Down
            temp = li[irow][icol]
            for j in xrange(irow, endRow - 1):
                temp1 = li[j + 1][icol]
                li[j + 1][icol] = temp
                temp = temp1
            irow = M - i - 1
            # print output(li)
            
            # Right
            icol += 1
            for j in xrange(icol, endCol):
                temp1 = li[irow][j]
                li[irow][j] = temp
                temp = temp1
            # print output(li),temp
            
            # UP
            icol = endCol - 1
            irow = irow - 1
            
            for j in xrange(irow, srow - 1, -1):
                temp1 = li[j][icol]
                li[j][icol] = temp
                temp = temp1
                
            # print output(li),temp
            
            # Left
            icol = icol - 1
            irow = srow
            
            for j in xrange(icol, scol - 1, -1):
                temp1 = li[irow][j]
                li[irow][j] = temp
                temp = temp1
            # print output(li),temp

M, N, R = map(int, raw_input().split())
li = []
for i in xrange(M):
    li.append(map(int, raw_input().split()))

rotateMatrix(li, R)
output(li)
    
# print li
