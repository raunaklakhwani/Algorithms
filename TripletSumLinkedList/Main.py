import random
class Node :
    def __init__(self, data, previous, next):
        self.data = data
        self.next = next
        self.previous = previous

def getList(inp):
    head = None
    tail = None
    for e in inp:
        if head is None:
            head = Node(e, None, None)
            tail = head
        else:
            tail.next = Node(e, tail, None)
            tail = tail.next
            
    return head

def printList(head):
    while head is not None:
        print head.data,
        head = head.next
    print

def partition(start, end, key, order):
    pivot = key.data
    temp = start
    tempPrevious = temp.previous
    
    if order == "ASC":
        while start is not end:
            if pivot > start.data:
                start.data, temp.data = temp.data, start.data
                tempPrevious = temp
                temp = temp.next
            start = start.next
        key.data, tempPrevious.data = tempPrevious.data, key.data
        return tempPrevious
    elif order == "DESC":
        while start is not end:
            if pivot < start.data:
                start.data, temp.data = temp.data, start.data
                tempPrevious = temp
                temp = temp.next
            start = start.next
        key.data, tempPrevious.data = tempPrevious.data, key.data
        return tempPrevious
        

def quickSortUtil(start, end, order):
    if start is not None and start.next is not None and start is not end:
        key = start
        pos = partition(start.next, end, key, order)
        quickSortUtil(start, pos, order)
        quickSortUtil(pos.next, end, order)

def quickSort(head, order):
    originalHead = head
    quickSortUtil(originalHead, None, order)


def generateRandomNumbersList():
    length = random.randint(1, 10)
    inp = [0] * length
    for i in xrange(length):
        inp[i] = random.randint(1, 100)
    return inp
"""
Time complexity is O(n*n) as element of b and c list are accessed exclusively
"""   
def findTriplet(f, s, t, X):
    headF = f
    while headF is not None:
        dataF = headF.data
        headS = s
        while headS is not None:
            dataS = headS.data
            headT = t
            while headT is not None:
                dataT = headT.data
                su = dataF + dataS + dataT
                if su == X:
                    return (dataF, dataS, dataT)
                elif su > X:
                    headT = headT.next
                else:
                    break
            headS = headS.next
        headF = headF.next
    return (None, None, None) 
    
if __name__ == '__main__':
    f = getList([12, 6, 29])
    s = getList([23, 5, 8])
    t = getList([90, 20, 59])
    X = 110
    
    # quickSort(f, "ASC")
    quickSort(s, "ASC")
    quickSort(t, "DESC")
    
    printList(f)
    printList(s)
    printList(t)
    
    print findTriplet(f, s, t, X)
    
    
