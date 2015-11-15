from collections import defaultdict


def getSuffixArrayUtil(s,order,indexes):
    result = []
    bucket = defaultdict(list)
    for i in indexes:
        bucket[s[i:i + order]].append(i)
    
    for key in sorted(bucket.keys()):
        value = bucket[key]
        if len(value) > 1:
            result += getSuffixArrayUtil(s, order << 1, value)
        else:
            result += [value[0]]
            getSuffixArray.rsa[value[0]] = getSuffixArray.index
            getSuffixArray.index += 1
            
    
    return result
    
    

def getSuffixArray(s):
    N = len(s)
    getSuffixArray.rsa = [-1] * N
    getSuffixArray.index = 0
    sa = getSuffixArrayUtil(s, 1,xrange(N))
    rsa = getSuffixArray.rsa
    
    
    
    lcp = N * [None]
    h = 0
    for i in range(N):
        if rsa[i] > 0:
            j = sa[rsa[i] - 1]
            while i != N - h and j != N - h and s[i + h] == s[j + h]:
                h += 1
            lcp[rsa[i]] = h
            if h > 0:
                h -= 1
    if N > 0:
        lcp[0] = 0
    
    
    
    return sa,rsa,lcp
    
    
if __name__ == '__main__':
    s = "ALKA"
    print getSuffixArray(s)