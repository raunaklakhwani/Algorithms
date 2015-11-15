from decimal import Decimal

for t in xrange(input()):
    N, M = map(int, raw_input().split())
    li = map(int, raw_input().split())
    pre = [1] * N
    for i in xrange(N):
        if i > 0:
            pre[i] = pre[i - 1] * li[i]
        else:
            pre[i] = li[i]
    
    out = "Case #" + str(t + 1) + ":"   
    print out     
    for q in xrange(M):
        a, b = map(int, raw_input().split())
        l = b - a + 1
        if a == 0:
            pa = 1
        else:
            pa = pre[a - 1]
        
        
        p = pre[b] / pa
        result = pow(p, 1 / Decimal(l))
        print round(result, 6)
        
         
        
