from random import  randint
N = 142
def computeParity1(num):
    parity = 0
    while num != 0:
        if num & 1:
            parity = parity ^ (num & 1)
        num = num >> 1
    return parity

def computeParity2(num):
    '''
    The idea is that when you and a number with (number - 1) then
    its lowest set bit is cleared.
    '''
    parity = 0
    while num:
        parity = parity ^ 1
        num = num & (num - 1)
    return parity


def generateRandom():
    num = randint(0, 100)
    return num

if __name__ == '__main__':
    
    
    print bin(N), computeParity1(N)
    print bin(N), computeParity2(N)
    print "____________________________"
    
    for i in xrange(10):
        num = generateRandom()
        print bin(num), computeParity1(num)
        print bin(num), computeParity2(num)
        print "____________________________"
        
        
