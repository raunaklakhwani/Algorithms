#http://www.careercup.com/question?id=5200686994161664
def getSubsetCountNaive(inp, A, B):
    result = 0
    count = 0
    for i in xrange(len(inp)):
        result = 0
        for j in xrange(i, len(inp)):
            result += inp[j]
            if result >= A and result <= B:
                count += 1
                
    return count

def getSubsetCountUtil(inp, start, end, A, B):
    if start == end:
        return 1 if inp[start] >= A and inp[start] <= B else 0
    else:
        ans = 0
        mid = start + ((end - start) >> 1)
        left = getSubsetCountUtil(inp, start, mid, A, B)
        right = getSubsetCountUtil(inp, mid + 1, end, A, B)
        ans += (left + right)
        p1 = p2 = start
        for i in xrange(mid + 1, end + 1):
            while p1 <= mid and (inp[i] - inp[p1]) >= A:
                p1 += 1
                
            while p2 <= mid and (inp[i] - inp[p2]) > B:
                p2 += 1
                
            if p1 >= p2:
                ans += (p1 - p2)
                
        
        a = start
        b = mid + 1
        temp = []
        for i in xrange(start, end + 1):
            if a <= mid and b <= end:
                if inp[a] <= inp[b]:
                    temp.append(inp[a])
                    a += 1
                else:
                    temp.append(inp[b])
                    b += 1
            elif a <= mid:
                temp.append(inp[a])
                a += 1
            else:
                temp.append(inp[b])
                b += 1
        
        j = 0             
        for i in xrange(start, end + 1):
            inp[i] = temp[j]
            j += 1
            
        return ans
            
            
            
        

def getSubsetCount(inp, A, B):
    for i in xrange(1, len(inp)):
        inp[i] += inp[i - 1]
    
    ans = getSubsetCountUtil(inp, 0, len(inp) - 1, A, B)
    return ans

if __name__ == '__main__':
    inp = [4, 2, 8, -1, 7, 2, -3]
    A, B = 0, 10
    
    #===========================================================================
    # inp = [1,2,3]
    # A,B = 0,3
    # 
    #===========================================================================
    
    
    print getSubsetCountNaive(inp, A, B)
    print getSubsetCount(inp, A, B)