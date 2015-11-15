if __name__ == '__main__':
    s1 = "cbacdcbc"
    s1 = "bcabc"
    
    h = {}
    
    i = len(s1) - 1
    n = [-1] * len(s1)
    v = {}
    while i >= 0:
        if h.get(s1[i]):
            n[i] = h[s1[i]]
            h[s1[i]] = i
        else:
            h[s1[i]] = i
            n[i] = -1
        i -= 1
    print n
    
    result = ""
    i = 0
    while i < len(s1):
        
        if v.get(s1[i]) is None:
            j = i + 1
            minimum = s1[i]
            minIndex = i
            while n[i] != -1 and j < len(s1):
                if n[j] == -1 and v.get(s1[j]) is None:
                    if minimum > s1[j]:
                        minimum = s1[j]
                        minIndex = j
                    break
                else:
                    if v.get(s1[j]) is None:
                        if minimum > s1[j]:
                            minimum = s1[j]
                            minIndex = j
                j += 1
            
            
            if minimum == s1[i]:
                result += s1[i]
                v[s1[i]] = True
                i += 1
            else:
                result += minimum
                v[minimum] = True
                i = minIndex + 1
        else:
            i += 1
            
    print result
            
            
        
        
                    
            
            
        
    
