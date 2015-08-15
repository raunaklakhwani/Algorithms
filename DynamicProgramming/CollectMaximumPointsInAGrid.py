# URL : http://www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals/

def getMaximumPointsInAGridUtil(inp, r1, c1, r2, c2, erow, ecol):
    #print r1,c1,r2,c2
    if r1 == erow and r2 == erow and c1 == 0 and c2 == ecol:
        return inp[erow][0] + inp[erow][ecol]
    elif c1 == c2 or r1 > erow or r2 > erow:
        return float("-inf")
    else:
        nextRow = r1 + 1
        startColumn1 = (c1 - 1) if (c1 - 1) >= 0 else c1
        endColumn1 = (c1 + 1) if (c1 + 1) <= ecol else ecol
        startColumn2 = (c2 - 1) if (c2 - 1) >= 0 else c2
        endColumn2 = (c2 + 1) if (c2 + 1) <= ecol else ecol
        maximum = float("-inf")
        for col1 in xrange(startColumn1, endColumn1 + 1):
            for col2 in xrange(startColumn2, endColumn2 + 1):
                ans = inp[r1][c1] + inp[r2][c2] + getMaximumPointsInAGridUtil(inp, nextRow, col1, nextRow, col2, erow, ecol)
                maximum = max(ans, maximum)
        return maximum
    
def getMaximumPointsInAGrid(inp):
    if len(inp):
        erow = len(inp) - 1
        ecol = len(inp[0]) - 1
        return getMaximumPointsInAGridUtil(inp, 0, 0, 0, ecol, erow, ecol)
    else:
        return float("-inf")
    print

if __name__ == '__main__':
    inp = [[3, 6, 8, 2], [5, 2, 4, 3], [1, 1, 20, 10], [1, 1, 20, 10], [1, 1, 20, 10]]
    #inp = [[1, 2], [3, 4]]
    print getMaximumPointsInAGrid(inp)
    
