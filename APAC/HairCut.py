from heapq import heappush, heappop, heapify
from fractions import gcd

def getLCM(a, b):
    return (a * b) / gcd(a, b)
    

def getLCMList(M):
    result = 1
    for i in M:
        result = getLCM(result, i)
    return result

def getCycleLength(M):
    ans = 0
    lcm = getLCMList(M)
    for i in M:
        ans += (lcm / i)
    return ans

def getBarberNumberUtil(M, N, B):
    cycleLength = getCycleLength(M)
    N = N % (cycleLength)
    if N != 0:
        result = getBarberNumber(M, N, B)
    else:
        minimum = float("inf")
        for i,v in enumerate(M):
            if minimum >= v:
                minimum = v
                result = i + 1
    return result
        
    
        
    


def getBarberNumber(M, N, B):
    
    if N <= len(M):
        barberNumber = N
    else:
        #=======================================================================
        # customer = 0
        # time = 0
        # while True:
        #     for i in xrange(B):
        #         if time % M[i] == 0:
        #             if customer == N:
        #                 return (i + 1)
        #             customer += 1
        #=======================================================================
        
        heap = [((M[i - 1], i))for i in xrange(1, len(M) + 1)]
        heapify(heap)
        barberNumber = len(M)
        for i in xrange(1, N - B + 1):
            time, barberNumber = heappop(heap)
            heappush(heap, ((time + M[barberNumber - 1], barberNumber)))
    return barberNumber


if __name__ == '__main__':
    for t in xrange(input()):
        B, N = map(int, raw_input().split())
        M = map(int, raw_input().split())
        
        if N <= len(M):
            result = N
        else:
            result = getBarberNumberUtil(M, N, B)
            
        
        # print N,M,result   
        out = "Case #" + str(t + 1) + ": " + str(result)
        print out
            
