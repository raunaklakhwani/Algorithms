s = "abaaba"


first = ord(s[0])
Firstlength = 1
secondLength = 0
second = 0
m = s[0]
chance = 2
for element in s[1:]:
    
    
    if chance & 1:
        # pop from B and add element to second
        second = second - (10 ** (secondLength - 1)) * ord(m[len(m) / 2])
        second = second * 10 + ord(element)
        
    else:
        if second == 0:
            second = ord(element)
            secondLength = 1
        else:
            second = second * 10 + ord(element)
            secondLength += 1
            first = (10 ** Firstlength) * ord(m[len(m) / 2]) + first
            Firstlength += 1
    
    m = m + element
    chance = chance + 1
            
    print m,m == m[::-1] 
    
            
        
    
    
