# Run ENcoding

s = "AABBC"
s = "AAAAAAABB"


def compressString(s, nl):
    s = list(s)
    p1 = 0
    prev = None
    c = 0
    i = 0
    
    while i < len(s):
        if prev is None:
            prev = s[i]
            c = 1
        elif prev == s[i]:
            c += 1
        else:
            s[p1] = prev
            p1 += 1
            while c:
                s[p1] = str(c % 10)
                p1 += 1
                c = c / 10
            
            prev = s[i]
            c = 1
        i += 1
    else:
        s[p1] = prev
        p1 += 1
        while c:
            s[p1] = str(c % 10)
            p1 += 1
            c = c / 10
        
    
    
    return "".join(s[:p1])
    
def expandString(s, nl):
    i = len(s) - 1
    s = list(s + " " * (nl - len(s)))
    h = len(s) - 1
    prev = None
    c = 0
    while i >= 0:
        if prev is None:
            prev = s[i]
            c = 1
        elif prev == s[i]:
            c += 1
        else:
            while c:
                s[h] = str(c % 10)
                c = c / 10
                h -= 1
            s[h] = prev
            h -= 1
            prev = s[i]
            c = 1
        i -= 1
    else:
        while c:
            s[h] = str(c % 10)
            c = c / 10
            h -= 1
        s[h] = prev
        h -= 1
            
    
        
    
    return "".join(s)
    

def getFinalCount(s):
    prev = None
    res = 0
    for i in s:
        if prev is None:
            prev = i
            c = 1
        elif prev == i:
            c += 1
        else:
            res = res + 1 + len(str(c))
            prev = i
            c = 0
    else:
        res = res + 1 + len(str(c))
    return res

nl = getFinalCount(s)

if nl > len(s):
    print expandString(s, nl)
else:
    print compressString(s, nl)





            
        
        
