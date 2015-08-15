s = "abcdefghijklm"
factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800 , 479001600 , 6227020800]


def getFixed(N, x, g):
    # print N,x,g
    m = 0
    for ind, i in enumerate(x):
        j = m + factorial[g]
        if j >= N:
            return ind, N - m
        m = j
        
        
for i in xrange(input()):
    n = input()
    x = [a for a in s]
    pos = 0
    f = ""
    while pos < len(s):
        ind, u = getFixed(n, x, len(s) - pos - 1)
        f = f + str(x[ind])
        del x[ind]
        x.sort()
        n = u 
        pos += 1
    print f