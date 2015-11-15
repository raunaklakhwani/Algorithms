from collections import defaultdict
from math import ceil, floor
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, key, count):
        self.key = key
        self.count = count
        


def getMinimumTime(li):
    h = {}
    for i in li:
        if h.get(i):
            h.get(i).count += 1
            
        else:
            h[i] = Node(i, 1)
        
    heap = []
    for key, node in h.items():
        heap.append([-1 * key, node])
        
    heapify(heap)
    
    time = 0
    
    while len(heap):
        key, node = heappop(heap)
        mTime = node.key
        count = node.count
        del h[mTime]
        
        secondTop = ceil(mTime / 2.0)
        if len(heap):
            if secondTop < (-1 * heap[0][0]):
                secondTop = -1 * heap[0][0]
        
        if mTime < count + secondTop:
            time += mTime
            break
        
        time += count
        if mTime & 1:
            # odd
            f = int(floor(mTime / 2.0))
            if h.get(f):
                h.get(f).count += count
            else:
                h[f] = Node(f, count)
                heappush(heap, [-1 * f, h[f]])
                
            c = int(ceil(mTime / 2.0))
            if h.get(c):
                h.get(c).count += count
            else:
                h[c] = Node(c, count)
                heappush(heap, [-1 * c, h[c]])
                
        else:
            # even
            f = mTime / 2
            if h.get(f):
                h.get(f).count += (count << 1)
            else:
                h[f] = Node(f, (count << 1))
                heappush(heap, [-1 * f, h[f]])
            
    
    return int(time)

print getMinimumTime([9,3,1])

for t in xrange(input()):
    D = input()
    li = map(int, raw_input().split())
    result = getMinimumTime(li)
    out = "Case #" + str(t + 1) + ": " + str(result)
    print li,out
