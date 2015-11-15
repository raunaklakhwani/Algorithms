from collections import defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop

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


class SymbolDictObject:
    def __init__(self):
        self.keys = []
        self.timeList = []
        self.minTime = None
        self.lastTime = None
        
s = raw_input().split()
N = int(s[1])

symbolMap = defaultdict(lambda : SymbolDictObject())

for z in xrange(N):
    timequery = raw_input().split()
    time = int(timequery[0])
    symbol = timequery[1]
    symbolObject = symbolMap[symbol]
    
    if symbolObject.minTime is None:
        symbolObject.minTime = time
        symbolObject.lastTime = time
        symbolObject.keys.append(time)
        fieldMap = defaultdict(list)
        symbolObject.timeList.append(fieldMap)
    elif time == symbolObject.lastTime:
        fieldMap = symbolObject.timeList[-1]
    else:
        symbolObject.lastTime = time
        symbolObject.keys.append(time)
        fieldMap = defaultdict(list)
        symbolObject.timeList.append(fieldMap)
        
    i = 2
    if len(timequery) > 2:
        i = 2
        while i < len(timequery):
            fieldName =  timequery[i]
            fieldValue = int(timequery[i + 1])
            fieldMap[fieldName].append(fieldValue)
            i += 2
            
print "tickfile completed"

while True:
    q = raw_input()
    if len(q) == 0:
        break
    q = q.split()
    commandType = q[0]
    if commandType == "max":
        st = int(q[1])
        et = int(q[2])
        symbol = q[3]
        field = q[4]
        K = int(q[5])
        keys = symbolMap[symbol].keys
        indexLeft = bisect_left(keys, st)
        indexRight = bisect_right(keys, et)
        timeList = symbolMap[symbol].timeList
        
        heap = []
        for i in xrange(indexLeft,indexRight):
            time = i
            fieldMap = timeList[time]
            if fieldMap.get(field):
                items = fieldMap.get(field)
                for item in items:
                    insertInHeap(heap, item, K)
        
        printHeapInDescending(heap)
        print
        
    elif commandType == "sum":
        st = int(q[1])
        et = int(q[2])
        symbol = q[3]
        field = q[4]
        keys = symbolMap[symbol].keys
        indexLeft = bisect_left(keys, st)
        indexRight = bisect_right(keys, et)
        timeList = symbolMap[symbol].timeList
        
        summation = 0
        for i in xrange(indexLeft,indexRight):
            time = i
            fieldMap = timeList[time]
            if fieldMap.get(field):
                items = fieldMap.get(field)
                if len(items) > 1:
                    summation += sum(items)
                else:
                    summation += items[0]
        print summation
        
    elif commandType == "product":
        st = int(q[1])
        et = int(q[2])
        symbol = q[3]
        field1 = q[4]
        field2 = q[5]
        keys = symbolMap[symbol].keys
        indexLeft = bisect_left(keys, st)
        indexRight = bisect_right(keys, et)
        timeList = symbolMap[symbol].timeList
        
        
        product = 0
        for i in xrange(indexLeft,indexRight):
            time = i
            fieldMap = timeList[time]
            if fieldMap.get(field1) and fieldMap.get(field2):
                itemsA = fieldMap.get(field1)
                itemsB = fieldMap.get(field2)
                
                for i in xrange(len(itemsA) if len(itemsA) <= len(itemsB) else len(itemsB)):
                    product += (itemsA[i] * itemsB[i])
                
        print product
        
    elif commandType == "delta":
        print
        
        
        
        
    
        
    
        
        
        
        
        
        
        
        
    
    
        



