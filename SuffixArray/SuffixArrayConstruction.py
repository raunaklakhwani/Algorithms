from collections import defaultdict
s = "ABAB1BABA2ABBA3"
s = "JACKaDANIELb"
s = "ABABBAABB"

def getSuffixArray(s):
    '''
    This construction algorithm will take a lot of time O(N^2 lg N).
    This is due to sorting of strings.
    '''
    return sorted(xrange(len(s)), key=lambda i : s[i:])

def sort_bucket(str, bucket, order): 
    d = defaultdict(list) 
    for i in bucket: 
        key = str[i:i + order] 
        d[key].append(i) 
    result = [] 
    for k, v in sorted(d.iteritems()): 
        if len(v) > 1: 
            result += sort_bucket(str, v, order * 2) 
        else: 
            result.append(v[0]) 
    return result 

def suffix_array_ManberMyers(str): 
    return sort_bucket(str, (i for i in range(len(str))), 1) 

print getSuffixArray(s)
print suffix_array_ManberMyers(s)

for i in getSuffixArray(s):
    print i,s[i:]
    
