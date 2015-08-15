l = [2,5,3]
cache = [0] * 501
cache[0] = 1
cache[1] = (1, 1 , 1)
cache[2] = (8, 13, 7)


ind = 2
def fillData(n):
    global ind
    a, b, N = cache[ind]
    while True:
        a, b = b, a + b
        N += 1
        l = len(str(b))
        if l != ind:
            cache[l] = (a,b, N)
            ind = l
        if l == n:
            break

for i in xrange(len(l)):
    n = l[i]
    if cache[n] != 0:
        print cache[n][2]
    else:
        fillData(n)
        print cache[n][2]
        
    
    
    
    
