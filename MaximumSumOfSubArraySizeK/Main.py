from _collections import deque


def getMaximumOfSubarraysOfSizeK(inp, k):
    maximum = []
    for i in xrange(0, len(inp) - k + 1):
        maximum.append(max(inp[i:i + k]))
        
    return maximum


def getMaximumOfSubarraysOfSizeKSmart(inp,k):
    maximum = []
    dq = deque([])
    for i in xrange(k):
        while len(dq) and inp[i] > inp[dq[-1]]:
            dq.pop()
        dq.append(i)
    
    for i in xrange(k,len(inp)):
        maximum.append(inp[dq[0]])
        while len(dq) and inp[i] > inp[dq[-1]]:
            dq.pop()
        while len(dq) and dq[0] < i-k:
            dq.popleft()
        dq.append(i)
    if len(dq):
        maximum.append(inp[dq[0]])
    return maximum

if __name__ == '__main__':
    K = 3
    inp = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    print getMaximumOfSubarraysOfSizeK(inp, K)
    print getMaximumOfSubarraysOfSizeKSmart(inp, K)
    
