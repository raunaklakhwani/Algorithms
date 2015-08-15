maximum = 5000001
cache = [0] * maximum
cache[1] = 1
ansCache = [0] * maximum
ansCache[1] = 1





def getLength(num):
    if num < maximum:
        if cache[num] == 0:
            if num & 1 == 1:
                temp = (num + num + num + 1)
                tempLength = getLength(temp >> 1)
                if temp < maximum:
                    cache[temp] = 1 + tempLength
                cache[num] = 2 + tempLength
            else:
                cache[num] = 1 + getLength(num >> 1)
        return cache[num]
    else:
        count = 0
        while(num >= maximum):
            if num & 1 == 1:
                count = count + 2
                num = (num + num + num + 1) >> 1
            else:
                count += 1 
                num = num >> 1
        
        return count + getLength(num)
            
    


    
i = 0 
for _ in xrange(input()):
    N = input()
    if ansCache[N] == 0 :
        for i in xrange(i+1,N+1):
            c = getLength(i)
            if cache[ansCache[i-1]] > c:
                ansCache[i] = ansCache[i-1]
            else:
                ansCache[i] = i
        
    print ansCache[N]