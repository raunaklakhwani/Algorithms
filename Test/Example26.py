#http://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/

def getRecurDigits(N):
    r = 1
    map = {}
    c = 0
    while r: 
        r = (r * 10) % N
        if map.get(r):
            break
        map[r] = 1
        c += 1
    return c


# print getRecurDigits(983)
if __name__ == '__main__':
    N = 1000
    maximum = float("-inf")
    for i in xrange(1, N):
        maximum = max(maximum, getRecurDigits(i))
    print maximum
