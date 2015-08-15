# URL : http://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/
import sys
sys.setrecursionlimit(100000)
N = 143

def getMinimumNumberOfSquaresUtil(N):
    if N < len(getMinimumNumberOfSquares.cache):
        if N == 0:
            return 0
        elif getMinimumNumberOfSquares.cache[N] != 0:
            return getMinimumNumberOfSquares.cache[N]
        else:
            i = 2
            minimum = N
            while i*i <= N:
                ans = 1 + getMinimumNumberOfSquaresUtil(N - i*i)
                if ans < minimum:
                    minimum = ans
                i = i + 1
            getMinimumNumberOfSquares.cache[N] = minimum
            return minimum
    else:
        i = 2
        minimum = N
        while i*i <= N:
            ans = 1 + getMinimumNumberOfSquaresUtil(N - i*i)
            if ans < minimum:
                minimum = ans
            i = i + 1
        return minimum
        
    
def getMinimumNumberOfSquares(N):
    getMinimumNumberOfSquares.cache = [0] * N
    getMinimumNumberOfSquares.cache[1] = 1
    getMinimumNumberOfSquares.cache[2] = 2
    getMinimumNumberOfSquares.cache[3] = 3
    return getMinimumNumberOfSquaresUtil(N)
    
if __name__ == '__main__':
    for i in xrange(10000,10100):
        print i,getMinimumNumberOfSquares(i)
