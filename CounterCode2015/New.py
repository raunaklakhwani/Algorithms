'''
8 3
6 7
2 4
1 8

8 3
4 6
2 7
1 8
'''
from collections import defaultdict
N,M = map(int,raw_input().split())
li = []

for _ in xrange(M):
    li.append(map(int,raw_input().split()))
    
li.sort(key = lambda item: item[0], reverse = True)

#print li
r = 0
h = {}

i = 1
h[(li[0][0],li[0][1])] = 1
while i < M:
    a1,b1 = li[i]
    j = i - 1
    while j >= 0:
        a2,b2 = li[j]
        if a1 <= a2 and b1 >= b2:
            h[(a1,b1)] = h[(a2,b2)] + 1
            break
        j -= 1
    else:
        h[(li[i][0],li[i][1])] = 1
    i += 1


#print h
    
x = sorted(list(h.iteritems()),key = lambda item:item[1])  
x1 = defaultdict(list)
for l in x:
    x1[l[1]].append(l[0])
    
print x1

r = 1
ans = 0
resAns = []
while True:
    if x1.get(r):
        inner = x1[r]
        
        for a1,b1 in inner:
            tempR = r + 1
            while x1.get(tempR):
                outer = x1[tempR]
                breakFlag = False
                for a2,b2 in outer:
                    if a2 <= a1 and b2 >= b1:
                        if a1 -1 >= a2 and a1 - 1 <= b2:
                            resAns.append((a1-1,a1))
                            #print a1-1,a1
                            ans += 1
                            breakFlag = True
                        if b1 + 1 >= a2 and b1 + 1 <= b2:
                            resAns.append((b1,b1+1))
                            #print b1,b1+1
                            ans += 1
                            breakFlag = True
                        
                        if breakFlag:    
                            break
                
                if breakFlag:
                    break
                tempR += 1
                
            
            
            #===================================================================
            # for a2,b2 in outer:
            #     if a2 <= a1 and b2 >= b1:
            #         if a1 -1 >= a2 and a1 - 1 <= b2:
            #             resAns.append((a1-1,a1))
            #             #print a1-1,a1
            #             ans += 1
            #         if b1 + 1 >= a2 and b1 + 1 <= b2:
            #             resAns.append((b1,b1+1))
            #             #print b1,b1+1
            #             ans += 1
            #===================================================================
                        
                    #===========================================================
                    # if a2 - 1 >= a1 and a2 - 1 <= b1:
                    #     ans += 1
                    #     
                    # if b2 + 1 >= a1 and b2 + 1 <= a2:
                    #     ans += 1
                    #===========================================================
                    
        r += 1
    else:
        break
    
print ans
resAns.sort()
for i in resAns:
    print i[0],i[1]
  
    

