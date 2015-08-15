

def getNextLargerNumber(N):
    numFound = None
    s = list(str(N))
    for i in xrange(len(s) - 1, -1 , -1):
        if s[i-1] < s[i]:
            index = i
            for j in xrange(i+1,len(s)):
                if s[index] > s[j] :
                    index = j
            
            s[i-1],s[index] = s[index],s[i-1]
            s = s[:i] + sorted(s[i:])
            numFound = "".join(s)
            break
        
    
    return numFound

if __name__ == '__main__':
    
    for i in xrange(1,100):
        print i,getNextLargerNumber(i)
    
    print 12785,getNextLargerNumber(12785)
    