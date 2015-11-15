def bruteForceCheck(s,r):
    if s[0] == r[0] and s[1] == r[1] and s[2] == r[2]:
        return True
    else:
        s[0],s[1],s[2] = s[2],s[0],s[1]
        if s[0] == r[0] and s[1] == r[1] and s[2] == r[2]:
            return True
        else:
            s[0],s[1],s[2] = s[2],s[0],s[1]
            if s[0] == r[0] and s[1] == r[1] and s[2] == r[2]:
                return True
    return False


s = "1342"
r = "4132"

s = list(s)
r = list(r)

possible = None

ind = len(r) - 1
while possible is None:
    if ind < 3:
        possible = bruteForceCheck(s,r)
    else:
        if r[ind] == s[ind]:
            ind -= 1
            if ind < 0:
                possible = True
                break
        else:
            sind = s.index(r[ind])
            diff = ind - sind
            if diff < 3:
                if diff == 1:
                    a = sind - 1
                    b = sind
                    c = ind
                    s[a],s[b],s[c] = s[c],s[a],s[b]
                elif diff == 2:
                    a = sind
                    b = sind + 1
                    c = ind
                    s[a],s[b],s[c] = s[b],s[c],s[a]
            else:
                while diff >= 3:
                    a = sind
                    b = sind + 1
                    c = sind + 2
                    s[a],s[b],s[c] = s[b],s[c],s[a]
                    diff -= 2
                    sind += 2
                    
                if diff == 1:
                    a = sind - 1
                    b = sind
                    c = ind
                    s[a],s[b],s[c] = s[c],s[a],s[b]
                elif diff == 2:
                    a = sind
                    b = sind + 1
                    c = ind
                    s[a],s[b],s[c] = s[b],s[c],s[a]
                    
        ind -= 1
        print s
                    
                
                
                
            
            
            
print possible
            
        
        
        