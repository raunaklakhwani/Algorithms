def getDigits(num):
    if num == 0:
        return 1
    else:
        i = 0
        while num:
            num = num / 10
            i += 1
        return i
    
maximum = 1000
primes = [1] * (maximum + 1)


prime = []
for i in xrange(2,len(primes)):
    if primes[i]:
        prime.append(i)
        for j in xrange(i<<1,len(primes),i):
            primes[j] = 0


def getResult():
    print
        
def getDivisors(num):
    i = 0
    h = {}
    while num != 1:
        i = 0
        while num % prime[i]:
            i += 1
            num = num / prime[i]
        if i:
            h[prime[i]] = i
        i += 1
    return h
        
            
        
        

    
l = "Laurence"
s = "Seymour"    
h = {}
h[0] = l
h[1] = s    

if __name__ == '__main__':
    for t in xrange(input()):
        N = input()
        
        
        turn = 0
        while True:
            d = getDigits(N)
            if primes[d]:
                winner = 1 - turn
                break
            div = getDivisors(N)
            if len(div) == 2:
                print
            else:
                r = len(div) - 2
                
            
            
            
        
        
        
        result = getResult()
        
        out = "Case #" + str(t + 1) + ": " + result
        print out