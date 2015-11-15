inp = [-2, -5, -6, -2, -3, -1, -5, -6]
#===============================================================================
# inp = [2, 1, 0, 2]
# inp = [2, 3, 1, 4]
#===============================================================================
currSum = inp[0]
maxSum = float("-inf")

for i in xrange(1,len(inp)):
    currSum = max(inp[i],currSum + inp[i])  
    maxSum = max(currSum,maxSum)

print maxSum

    
