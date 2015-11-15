from collections import defaultdict
from bisect import bisect_left,bisect_right
from heapq import heapify,heappop,heappush


s = raw_input().split()
N = int(s[1])

def insertInHeap(heap,item,K):
    if len(heap) < K:
        heappush(heap, item)
    elif item > heap[0]:
        heappop(heap)
        heappush(heap, item)
        
def printHeapInDescending(heap):
    if len(heap):
        pop = heappop(heap)
        printHeapInDescending(heap)
        print pop,
        

#timeMap = defaultdict(defaultdict(defaultdict(int)))
timeMap = defaultdict(lambda : defaultdict(lambda : defaultdict(int)))
for _ in xrange(N):
    timequery = raw_input().split()
    time = int(timequery[0])
    symbolMap = timeMap[time]
    
    if len(timequery) > 1:
        symbol = timequery[1]
        fieldMap = symbolMap[symbol]
        
        if len(timequery) > 2:
            i = 2
            while i < len(timequery):
                fieldName =  timequery[i]
                fieldValue = int(timequery[i + 1])
                fieldMap[fieldName] = fieldValue
                i += 2
    
#print timeMap
print "tickfile completed"


keys = sorted(timeMap.keys())

Q = input()
for _ in xrange(Q):
    q = raw_input().split()
    st = int(q[1])
    et = int(q[2])
    symbol = q[3]
    field = q[4]
    indexLeft = bisect_left(keys, st)
    indexRight = bisect_right(keys, et)
    
    summation = 0
    for i in xrange(indexLeft,indexRight):
        time = keys[i]
        symbolMap = timeMap[time]
        if symbolMap.get(symbol) and symbolMap.get(symbol).get(field):
            item = symbolMap.get(symbol).get(field)
            summation += item
    
    print summation
            
            
        

    
    
    
    
    
    
    

    
        
        
    
    
