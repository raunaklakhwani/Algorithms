from heapq import heapify, heappush, heappop
def myheapify(li):
    for i in xrange((len(li) - 1) / 2 - 1, -1, -1):
        actualHeapify(li, i)
        
def myheappush(li, item):
    li.append(item)
    actualHeapify(li, (len(li) - 2) / 2)


def topDownHeapify(li,ind,length):
    child1 = 2 * ind + 1
    child2 = (2 * ind + 2) if (child1 + 1) < length else 0
    minChild = -1
    if child2:
        minChild = child1 if li[child1] < li[child2] else child2
    else:
        minChild = child1
    
    while minChild < length and li[ind] > li[minChild]:
        li[ind], li[minChild] = li[minChild], li[ind]
        ind = minChild
        child1 = 2 * ind + 1
        child2 = (2 * ind + 2) if (child1 + 1) < length else 0
        minChild = -1
        if child2:
            minChild = child1 if li[child1] < li[child2] else child2
        else:
            minChild = child1
    
    
def myheappop(li):
    item = li[0]
    li[0] = li[-1]
    del li[-1]
    topDownHeapify(li, 0,len(li))
    return item 
        
def actualHeapify(li, ind):
    child1 = 2 * ind + 1
    child2 = (2 * ind + 2) if (child1 + 1) < len(li) else 0
    minChild = -1
    if child2:
        minChild = child1 if li[child1] < li[child2] else child2
    else:
        minChild = child1
        
    while ind >= 0 and li[ind] > li[minChild]:
        li[ind], li[minChild] = li[minChild], li[ind]
        ind = (ind - 1) / 2
        child1 = 2 * ind + 1
        child2 = (2 * ind + 2) if (child1 + 1) < len(li) else 0
        minChild = -1
        if child2:
            minChild = child1 if li[child1] < li[child2] else child2
        else:
            minChild = child1
        
def myHeapSort(li):
    length = len(li)
    
    for i in xrange(0,len(li)):
        length = length - 1
        li[0],li[length] = li[length],li[0]
        topDownHeapify(li, 0, length)
        #print li
    
    
    
    print li
        
    
    
    
def compare(li, li1):
    print "myli = " , li
    print "pythonli = " , li1    
       

    

if __name__ == '__main__':
    li = [8, 5, 1, 2, 7, 9, 13, 10]
    li1 = [8, 5, 1, 2, 7, 9, 13, 10]
    
    myheapify(li)
    heapify(li1)
    compare(li, li1)
    
    myheappush(li, 3)
    heappush(li1, 3)
    compare(li, li1)
    
    while len(li):
        print heappop(li1)
        print myheappop(li)
        compare(li, li1)
        print "_________________"
        
    li = [8, 5, 1, 2, 7, 9, 13, 10]
    myheapify(li)
    print li
    myHeapSort(li)
    
    

