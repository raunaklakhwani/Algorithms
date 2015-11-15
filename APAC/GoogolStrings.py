from math import log,ceil

def getCharacter(K):
    if not (K & K-1):
        return False
    else:
        n = int(ceil(log(K,2)))
        #print n
        return not getCharacter((1<<n) - K)

for i in xrange(input()):
    K = input()
    s = getCharacter(K)
    if s:
        s = 1
    else:
        s = 0
    out = "Case #" + str(i + 1) + ": " + str(s)
    print out
