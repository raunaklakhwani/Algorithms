from collections import Counter
import heapq
from math import ceil

class MaxHeap(object):
    def __init__(self, x):
        self.heap = [(-e[0],e[1]) for e in x.items()]
        heapq.heapify(self.heap)
    def push(self, value):
        heapq.heappush(self.heap, (-value[0],value[1]))
    def pop(self):
        pop = heapq.heappop(self.heap)
        return (-pop[0],pop[1])
    def getItems(self):
        return [(-item[0],item[1]) for item in self.heap]
    def getMax(self):
        return (-self.heap[0][0],self.heap[0][1])
    def len(self):
        return len(self.heap) 
    
def getMinMinutes(d,nonEmpty):
    minTime = 0
    heap = MaxHeap({})
    d = int(d)
    nonEmpty = map(int,nonEmpty.split())
    c = Counter(nonEmpty)
    keys = sorted(c.viewkeys(), reverse = True)
    
    for item in keys:
        heap.push((item,c[item]))
    
    while True:
        maxPanCakes,count = heap.pop()
        length = heap.len()
        heapMax = heap.getMax()[0] if length > 0 else 0
        maxElement = ceil(maxPanCakes/2.0) if ceil(maxPanCakes/2.0) > heapMax else heapMax 
        if maxElement != 0 :
            if count + maxElement <= maxPanCakes:
                minTime = minTime + count
                items = dict(heap.getItems())
                setItem(items, maxPanCakes/2, count)
                setItem(items, maxPanCakes - maxPanCakes/2, count)
                heap = MaxHeap(items)
            else :
                minTime = minTime + maxPanCakes
                break
        else:
            if count + ceil(maxPanCakes/2.0) <= maxPanCakes: 
                minTime = minTime + count
                items = dict(heap.getItems())
                setItem(items, maxPanCakes/2, count)
                setItem(items, maxPanCakes - maxPanCakes/2, count)
                heap = MaxHeap(items)
            else :
                minTime = minTime + maxPanCakes
                break
                
    return minTime

def setItem(items,item,count) :
    if items.get(item) is None:
        items[item] = count
    else:
        items[item] = items[item] + count
    

if __name__ == '__main__':
    #getMinMinutes("3", "3 1 3")
    with open("B-large-practice.in") as f:
        count = int(f.readline())
        for i in xrange(count):
            d = f.readline()
            nonEmpty = f.readline()
            print d, nonEmpty
            minTime = getMinMinutes(d, nonEmpty)
            
            print "Case #" + str(i + 1) + ": " + str(minTime)
            print '-------------------------'
    
