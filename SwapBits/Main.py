from random import randint
N = 42


def generateRandom():
    num = randint(0, 100)
    return num

def swapBits(N, i, j):
    if (N>>i) & 1 != (N>>j) & 1:
        N = N ^ (1 << i)
        N = N ^ (1 << j)
        
    
    #===========================================================================
    # ci = N & (1 << i)
    # cj = N & (1 << j)
    # print bin(ci),bin(cj)
    # if ci != cj:
    #     N = N ^ (1 << i)
    #     N = N ^ (1 << j)
    #===========================================================================
    
    return N

if __name__ == '__main__':
    i = 3 
    j = 6
    
    print bin(N), bin(swapBits(N, i, j))

