from heapq import heappush, heappop
def recurse(s1, s2, i, li, cache):
    if cache.get((s1, s2, i)) is not None:
        return cache[(s1, s2, i)]
    elif i == len(li):
        return True
    elif s1 + li[i] > G and s2 + li[i] > G:
        return False
    elif s1 + li[i] > G:
        ans = recurse(s1, s2 + li[i], i + 1, li, cache)
    elif s2 + li[i] > G:
        ans = recurse(s1 + li[i], s2, i + 1, li, cache)
    else:
        a = recurse(s1, s2 + li[i], i + 1, li, cache)
        b = recurse(s1 + li[i], s2, i + 1, li, cache)
        ans = a or b
        
    cache[(s1, s2, i)] = ans
    return ans
    
    
for _ in xrange(input()):
    N, G = map(int, raw_input().split())
    li = map(int, raw_input().split())
    li.sort(reverse=True)
    s1 = s2 = 0
    ans = recurse(s1, s2, 0, li,{})
    if ans:
        print "YES"
    else:
        print "NO"
        
        
        
    
    
            
    
    
        
        
        
