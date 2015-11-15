# URL : http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/

def isValid(currx, curry, N, li):
    return currx >= 0 and currx < N and curry >= 0 and curry < N and li[currx][curry] == -1

def getSolutionUtil(li, N, movesPossible, currX, currY, moveNum):
    #print moveNum
    if moveNum == N * N:
        # print moveNum
        print li
        return True

    for ix, iy in movesPossible:
        if isValid(currX + ix, currY + iy, N, li):
            li[currX + ix][currY + iy] = moveNum
            if getSolutionUtil(li, N, movesPossible, currX + ix, currY + iy, moveNum + 1):
                return True
            li[currX + ix][currY + iy] = -1
    
    return False
        
    
    
    

def getSolution(N):
    li = [[-1] * N for i in xrange(N)]
    '''
    In this the thing is you should keep (2,1) move earlier as it takes you to the result earlier. This is a heuristics.
    '''
    movesPossible = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    #movesPossible = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    li[0][0] = 0
    getSolutionUtil(li, N, movesPossible, 0, 0, 1)

if __name__ == '__main__':
    N = 8
    getSolution(N)
