
def getAns(a, b, N, K, P, steps, index, stair):
    #print index, stair
    
    if index > N:
        return (float("inf"), stair)
    elif index == N:
        if stair == 0:
            steps[stair][index] = (a[N], stair)
            return (a[N], stair)
        else:
            steps[stair][index] = (b[N], stair)
            return (b[N], stair)
    elif steps[stair][index] != -1:
        return steps[stair][index] 
    else:
        ans = float("inf")
        updatedStair = stair
        end = index + K + 1
        # end = len(a) if index + K + 1 >= len(a) else end
        
        for i in xrange(index + 1, end if end <= N + 1 else N + 1):
            firstAns, firstStair = getAns(a, b, N, K, P, steps, i, stair)
            secondAns, secondStair = getAns(a, b, N, K, P, steps, i, 1 - stair)
            
            if stair == 0:
                firstAns += a[index]
                secondAns += a[index]
            else:
                firstAns += b[index]
                secondAns += b[index]
                
            
            if firstAns <= P + secondAns:
                if ans > firstAns:
                    ans = firstAns
                    updatedStair = firstStair
            else:
                if ans > secondAns:
                    ans = P + secondAns
                    updatedStair = secondStair
        steps[stair][index] = (ans, updatedStair)
        return steps[stair][index]
    
        
            
for _ in xrange(input()):
    N, K, P = map(int, raw_input().split())
    a = [0] + map(int, raw_input().split())
    b = [0] + map(int, raw_input().split())
    steps = [[-1] * (N + 1) for i in xrange(2)]

    getAns(a, b, N, K, P, steps, 1, 0) 
    getAns(a, b, N, K, P, steps, 1, 1) 
    #print steps
    print min(steps[0][1][0], steps[1][1][0])
        
        
            

