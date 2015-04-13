import sys


def standingOvation(smax, shynessString):
    l = []
    for i in range(0,smax + 1):
        l.append((i,int(shynessString[i])))
    
    minimum = 0
    numPersonStood = 0
    #print l
    for s,p in l:
        if s > numPersonStood:
            minimum = minimum + s - numPersonStood
            numPersonStood = numPersonStood + s - numPersonStood
        numPersonStood = numPersonStood + p
        
    return minimum
        
    
        
if __name__ == '__main__':
    with open("A-large.in") as f:
        count = int(f.readline())
        for i in xrange(count):
            smax,shynessString = f.readline().split()
            result = str(standingOvation(int(smax),shynessString))
            print "Case #" + str(i + 1) + ": " + result
        
    
    