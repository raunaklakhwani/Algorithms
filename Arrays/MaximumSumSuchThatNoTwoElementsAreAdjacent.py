# URL : http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
inp = [3, 2, 5, 10, 7]
#===============================================================================
# inp = [2, 1, 0, 2]
# inp = [2, 3, 1, 4]
#===============================================================================

def getMaximumSum(inp, start, end):
    if start > end:
        return float("-inf")
    elif start == end:
        return inp[start]
    else:
        return max(inp[start] + getMaximumSum(inp, start + 2, end), inp[start + 1] + getMaximumSum(inp, start + 3, end))
    
print getMaximumSum(inp, 0, len(inp) - 1)
    
