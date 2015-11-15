def method1(li):
    ans = 0
    for i in xrange(1, len(li)):
        if li[i - 1] > li[i]:
            ans += (li[i - 1] - li[i])
    return ans
            

def method2(li):
    ans = 0
    rate = 0
    for i in xrange(1, len(li)):
        if li[i - 1] > li[i]:
            if rate < (li[i - 1] - li[i]):
                rate = (li[i - 1] - li[i])
                
    
    for i in xrange(len(li) - 1):
        if li[i] >= rate:
            ans += rate
        else:
            ans += li[i]
    return ans      

for t in xrange(input()):
    N = input()
    li = map(int, raw_input().split())
    m1 = method1(li)
    m2 = method2(li)
    out = "Case #" + str(t + 1) + ": " + str(m1) + " " + str(m2)
    print out
