# http://www.careercup.com/question?id=5693954190213120
inp = [1, 2, 3, 10, 25, 26, 30, 31, 32, 33]
inp = [1, 2, 3, 4, 7, 8, 9, 12, 13, 16]


def getCompressedListNaive(inp):
    start = 0
    end = 1
    prev = 0
    ans = []
    for i in xrange(1, len(inp)):
        if inp[end] - inp[prev] == 1:
            prev += 1
            end += 1
        else:
            ans.append((inp[start], inp[prev]))
            start = end
            prev = end
            end += 1
            
    ans.append((inp[start], inp[end - 1]))
    return ans
        

def getSmartCompressionList(inp):
    k = 0
    start = 0
    end = 0
    newEnd = start
    oldEnd = None
    ans = []
    while start < len(inp):
        #print "Roa"
        if oldEnd and oldEnd == end:
            ans.append((inp[start],inp[end]))
            start = end + 1
            k = 0
            end = start
            newEnd = start
            oldEnd = None
        
        
        newEnd = int(end + 2 ** k)
        if newEnd < len(inp):
            if inp[newEnd] - inp[end] == newEnd - end:
                k += 1
                oldEnd = end
                end = newEnd
            else:
                k -= 1
        else:
            k -= 1
            
    return ans
        
        
        
        
    
        
    
