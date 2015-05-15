from bisect import bisect_left
tail = []

            
        

def getIndex(num):
    j = len(active) - 1
    #print tail,num
    j = bisect_left(tail, num)
    j = j - 1
    #print "j = ",j
    #print "j = ", j, tail
    if j >= 0:
        n = active[j][:]
        n.append(num)  
    else:
        n = [num]
    if len(active) != j + 1:
        del active[j + 1]
        del tail[j + 1]
    active.insert(j+1,n)
    tail.insert(j+1,n[-1])
   
N = int(raw_input())
active = []
for i in xrange(N):
    num = int(raw_input())
    getIndex(num)
    #print "active = ",active
    #print "tail = ",tail
print len(active[-1])