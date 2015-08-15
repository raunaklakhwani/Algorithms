from math import log
def generatePowerSet(inp):
    '''
    The idea is to check the bots set of i where i range from 0 - (2 ^ n - 1).
    i & (i-1) clears the set bit from the LSB end
    i & ~(i - 1) gives the corresponding set bit.
    We take log of i & ~ (i - 1) to get the corresponding bit number. 
    '''
    out = []
    for i in xrange(2 ** len(inp)):
        do = []
        while i:
            n = int(log(i & ~(i - 1), 2))
            # print n
            do.append(inp[n])
            i = i & (i - 1)
        out.append(do)
    return out

def powerset(s):
    return [[s[j] for j in xrange(len(s)) if (i & (1 << j))] for i in xrange(1 << len(s))]

if __name__ == '__main__':
    inp = [1, 2, 3, 4]
    out = generatePowerSet(inp)
    print out
    print len(out)
    print powerset(inp)
    
