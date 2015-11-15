# URL : http://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/
inp = [4, 2, -3, 1, 6]
#===============================================================================
# inp = [2, 1, 0, 2]
# inp = [2, 3, 1, 4]
#===============================================================================
m = {}
currSum = 0
for i in xrange(len(inp)):
    currSum += inp[i]
    if m.get(currSum) is not None:
        print True
        break
    
    m[currSum] = i
else:
    print False    

    
