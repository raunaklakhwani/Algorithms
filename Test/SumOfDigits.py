pre = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

def calculateSumOfDigits(num):
    s = 0
    while num != 0:
        s = s + num % 10
        num = num / 10
    return s

def getDigits(num):
    digits = 0
    if num == 0:
        digits = 1
    else:
        while num != 0:
            digits += 1
            num = num / 10
    return digits



def calculateBruteForce(n):
    result = 0
    for i in xrange(1, n + 1):
        result += calculateSumOfDigits(i)
    return result

def getSum(n, digits):
    # print n,digits
    if n == 9:
        return 45
    else:
        return getSum(n / 10, digits - 1) * 10 + 45 * (10 ** (digits - 1))


def calculateSumSmartly(n):
    res = 0
    print n, "rr"
    if n > 9:
        digits = getDigits(n)
        po = 10 ** (digits - 1)
        # print digits
        x = getSum(po - 1, digits - 1)
        print x
        
        rem = n % (po)
        d = n / (po)
        
        res += d * (rem + 1) + calculateSumSmartly(rem)
        
        n = n - rem - 1
        y = n / (po)
        res += ((y+1) * x)
        res += (po * pre[y])
        return res
    else :
        return pre[n]
    
if __name__ == '__main__':
    n = 328
    brute = calculateBruteForce(n)
    result = 0
    print calculateSumSmartly(n)
    
    
    
    
    
    
