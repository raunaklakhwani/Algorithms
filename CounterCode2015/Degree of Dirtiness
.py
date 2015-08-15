def getLeftMinimum(li):
    m = li[0]
    ind = 0
    for j in xrange(1, len(li)):
        if li[j] < m:
            ind = j
            m = li[j]
        
    return ind

def getRightMinimum(li):
    m = li[-1]
    ind = len(li) - 1
    for j in xrange(len(li) - 2, -1, -1):
        if li[j] < m:
            ind = j
            m = li[j]
        
    return ind


for _ in xrange(1):
    N, M = 3,10
    
    if N & 1:
        a = (M / (2 * N)) * 2 
        li = [a] * N
        M = M - a * N
    else:
        a = M / N
        li = [a] * N
        M = M - a * N
    
    left = True
    finalInd = -1
    
    for i in xrange(M):
        if not left:
            ind = getRightMinimum(li)
            li[ind] += 1
            finalInd = ind
        else:
            ind = getLeftMinimum(li)
            li[ind] += 1
            finalInd = ind
        left = not left
    print finalInd + 1, li[finalInd] - 1
    
    
    
    
    
    
    
    
        
