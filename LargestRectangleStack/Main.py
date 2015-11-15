N = 1
hist = [2,3,4,5,6]
s = []

maxArea = 0

i = 0
while i < len(hist):
    h = hist[i]
    if len(s) == 0:
        s.append(i)
        i += 1
    else:
        top = s[-1]
        if h >= hist[top]:
            s.append(i)
            i += 1
        else:
            if len(s) > 0 and hist[s[-1]] > h:
                # i is right index
                # j is left index
                top = s.pop()
                
                j = s[-1] if len(s) > 0 else -1
                area = hist[top] * (i - j - 1)
                if area > maxArea:
                    maxArea = area
                    
while len(s) > 0:
    # i is right index
    # j is left index
    top = s.pop()
    
    j = s[-1] if len(s) > 0 else -1
    area = hist[top] * (i - j - 1)
    if area > maxArea:
        maxArea = area
        
print maxArea

                
            
    
    
            
            
