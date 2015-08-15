# URL : http://www.geeksforgeeks.org/count-numbers-that-dont-contain-3/
from random import randint
pre = [1,2,3,3,4,5,6,7,8,9]
def doesContainThree(num):
    contain = False
    while num:
        if num % 10 == 3:
            contain = True
            return contain
        num = num / 10
    return contain

def countNumbersThatDontContain3BruteForce(N):
    count = 0
    for i in xrange(1,N+1):
        if not doesContainThree(i):
            count += 1
    return count
            
def getDigits(num):
    digits = 0
    if num != 0:
        while num:
            digits += 1
            num = num / 10
        return digits  
    else:
        return 1      


def countFromZeroToTenToThePowerD(d):
    if d==1:
        return 9
    else:
        return 9 * countFromZeroToTenToThePowerD(d-1)

def countNumbersThatDontContain3Smartly(N):
    if N >= 0 and N <= 9:
        return pre[N]
    count = 0
    d = getDigits(N)
    k = 9 ** (d-1)
    ten = 10 ** (d-1)
    
    m = N / ten
    if m < 3:
        count += m * k + countNumbersThatDontContain3Smartly(N % ten)
    elif m > 3:
        count += (m-1) * k+ countNumbersThatDontContain3Smartly(N % ten)
    else:
        count += m * k
    return count
        
        
    

if __name__ == '__main__':
    N = 300
    print countNumbersThatDontContain3BruteForce(N)
    print countNumbersThatDontContain3Smartly(N)
    
    for i in xrange(100):
        r = randint(1,100)
        a =  countNumbersThatDontContain3BruteForce(r)
        b =  countNumbersThatDontContain3Smartly(r)
        print r,a, b-1, a==b-1
        print "_________________________________"
        
        
    
    