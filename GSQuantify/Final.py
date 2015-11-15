from collections import defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
from math import ceil

delta = 0

def getSegments(inp):
    segments = []
    for i in xrange(len(inp)):
        if len(segments) == 0:
            segments.append([inp[i]])
        else:
            if len(segments[-1]) == 1:
                segments[-1].append(inp[i])
            else:
                if segments[-1][-1][1] > segments[-1][-2][1]:
                    if inp[i][1] > segments[-1][-1][1]:
                        segments[-1].append(inp[i])
                    else:
                        segments.append([inp[i]])
                elif segments[-1][-1][1] < segments[-1][-2][1]:
                    if inp[i][1] < segments[-1][-1][1]:
                        segments[-1].append(inp[i])
                    else:
                        segments.append([inp[i]])
                else:
                    if inp[i][1] == segments[-1][-1][1]:
                        segments[-1].append(inp[i])
                    else:
                        segments.append([inp[i]])
    return segments

def getLineSlopeAndIntercept(inp):
    if len(inp) == 1:
        return (0,inp[0][1])
    sumx = sumy = sumsqx = sumxy = 0
    for i in xrange(len(inp)):
        x, y = inp[i]
        sumx += x
        sumy += y
        sumsqx += (x * x)
        sumxy += (x * y)
    
    ymean = (float)(sumy) / len(inp)
    xmean = (float)(sumx) / len(inp)
    
    slope = (sumxy - sumx * ymean) / (sumsqx - sumx * xmean)
    intercept = ymean - slope * xmean
    
    return (slope, intercept)

def getError(slope, intercept, inp):
    error = 0
    for x, y in inp:
        predict = slope * x + intercept
        error += ((predict - y) ** 2)
    return error
    
    
    
def insertInHeap(heap, item, K):
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
            fieldName = timequery[i]
            fieldValue = int(timequery[i + 1])
            fieldMap[fieldName].append(fieldValue)
            i += 2
            
print "tickfile completed"

while True:
    try:
        q = raw_input()
        if len(q) == 0:
            break
    except (EOFError):
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
        for i in xrange(indexLeft, indexRight):
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
        for i in xrange(indexLeft, indexRight):
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
        for i in xrange(indexLeft, indexRight):
            time = i
            fieldMap = timeList[time]
            if fieldMap.get(field1) and fieldMap.get(field2):
                itemsA = fieldMap.get(field1)
                itemsB = fieldMap.get(field2)
                
                for i in xrange(len(itemsA) if len(itemsA) <= len(itemsB) else len(itemsB)):
                    product += (itemsA[i] * itemsB[i])
                
        print product
        
    elif commandType == "delta":
        symbol = q[1]
        field = q[2]
        K = int(q[3])
        
        timeseries = []
        symbolObject = symbolMap[symbol]
        timeList = symbolObject.timeList
        for i in xrange(len(timeList)):
            if timeList[i].get(field):
                value = timeList[i].get(field)
                for item in value:
                    timeseries.append((symbolObject.keys[i], item))
                    
        maximumError = ceil(len(timeseries) / 2.0) * K
        
        segments = getSegments(timeseries)
        #print segments,maximumError
        errors = []
        coefficients = []
        
        for inp in segments:
            slope,intercept = getLineSlopeAndIntercept(inp)
            error = getError(slope, intercept, inp)
            coefficients.append((slope,intercept))
            errors.append(error)
        
        errorCurrent = 0
        
        i = 0
        final = 1
        while i < (len(segments)):
            slope,intercept = coefficients[i]
            error = errors[i]
            
            
            if i + 1 < len(segments):
                differentError = errors[i] + errors[i + 1]
                sameError = getError(slope, intercept, segments[i] + segments[i + 1])
                
                if differentError > sameError:
                    
                    segments[i] = segments[i] + segments[i + 1]
                    s,inter = getLineSlopeAndIntercept(segments[i])
                    e = getError(s, inter, segments[i])
                    if e <= sameError:
                        coefficients[i] = (s,inter)
                        errors[i] = e
                        errorCurrent += (e)
                    else:
                        errors[i] = sameError
                        errorCurrent += (sameError)
                    
                    del segments[i + 1]
                    del errors[i + 1]
                else:
                    errorCurrent += (differentError)
                    final += 1
                    
                if errorCurrent + (final * K) >= maximumError:
                    errorCurrent = maximumError
                    print int(ceil(errorCurrent)) 
                    break
            else:
                errorCurrent += (error)
            i += 1
        else:
            print int(ceil(errorCurrent + (final * K)))
            
        
        
        
