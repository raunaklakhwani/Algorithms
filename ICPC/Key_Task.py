#URL : http://daniel.lawrence.lu/blog/y2014m09d12/probs.pdf
'''
1 10
*........X
1 3
*#X
3 20
####################
#XY.gBr.*.Rb.G.GG.y#
####################
0 0
'''
from collections import deque
from collections import defaultdict

while True:
    R, C = map(int, raw_input().split())
    if R == 0:
        break
    
    li = []
    for i in xrange(R):
        li.append(list(raw_input().strip()))
     
    si = sj = None   
    for i in xrange(R):
        for j in xrange(C):
            if li[i][j] == "*":
                si = i
                sj = j
                break
    
    mask = 0
    q = deque([(si, sj, mask, 0)])
    visited = defaultdict(lambda : False)
    visited[(si, sj, mask)] = True
    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while len(q):
        si, sj, mask, count = q.popleft()
        #print si,sj,li[si][sj],mask,count,
        breakFlag = False
        if li[si][sj] == "X":
            breakFlag = True
        if not breakFlag:
            for dx, dy in adj:
                nextX = si + dx
                nextY = sj + dy
                if nextX >= 0 and nextX < R and nextY >= 0 and nextY < C and li[nextX][nextY] != "#":
                    if (li[nextX][nextY] == "." or li[nextX][nextY] == "*" or li[nextX][nextY] == "X") and not visited[(nextX, nextY, mask)]:
                        visited[(nextX, nextY, mask)] = True
                        q.append((nextX, nextY, mask, count + 1))
                    elif li[nextX][nextY] in ('r', 'g', 'b', 'y'):
                        if li[nextX][nextY] == 'r' and not visited[(nextX, nextY, mask)]:
                            nmask = mask | 1 << 3
                            visited[(nextX, nextY, nmask)] = True
                            q.append((nextX, nextY, nmask, count + 1))
                        elif li[nextX][nextY] == 'g' and not visited[(nextX, nextY, mask)]:
                            nmask = mask | 1 << 2
                            visited[(nextX, nextY, nmask)] = True
                            q.append((nextX, nextY, nmask, count + 1))
                        elif li[nextX][nextY] == 'b' and not visited[(nextX, nextY, mask)]:
                            nmask = mask | 1 << 1
                            visited[(nextX, nextY, nmask)] = True
                            q.append((nextX, nextY, nmask, count + 1))
                        elif li[nextX][nextY] == 'y' and not visited[(nextX, nextY, mask)]:
                            nmask = mask | 1
                            visited[(nextX, nextY, nmask)] = True
                            q.append((nextX, nextY, nmask, count + 1))
                    elif li[nextX][nextY] in ('R', 'G', 'B', 'Y'):
                        if li[nextX][nextY] == 'R' and not visited[(nextX, nextY, mask)] and (mask >> 3 & 1):
                            #mask = mask | 7
                            visited[(nextX, nextY, mask)] = True
                            q.append((nextX, nextY, mask, count + 1))
                        elif li[nextX][nextY] == 'G' and not visited[(nextX, nextY, mask)] and (mask >> 2 & 1):
                            #mask = mask | 11
                            visited[(nextX, nextY, mask)] = True
                            q.append((nextX, nextY, mask, count + 1))
                        elif li[nextX][nextY] == 'B' and not visited[(nextX, nextY, mask)] and (mask >> 1 & 1):
                            #mask = mask | 13
                            visited[(nextX, nextY, mask)] = True
                            q.append((nextX, nextY, mask, count + 1))
                        elif li[nextX][nextY] == 'Y' and not visited[(nextX, nextY, mask)] and (mask & 1):
                            #mask = mask | 14
                            visited[(nextX, nextY, mask)] = True
                            q.append((nextX, nextY, mask, count + 1))
        #print q
        if breakFlag:
            print count
            break
    else:
        print "The poor student is trapped!"
                    
        
        
        
        
    
    
    
                
