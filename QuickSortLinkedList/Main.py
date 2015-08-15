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
            tail.next = Node(e, tail,None)
            tail = tail.next
            
    return head

def printList(head):
    while head is not None:
        print head.data,
        head = head.next
    print
    
def getLength(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def partition(start,end,key):
    pivot = key.data
    temp = start
    tempPrevious = temp.previous
    while start is not end:
        if pivot < start.data:
            start.data,temp.data = temp.data,start.data
            tempPrevious = temp
            temp = temp.next
        start = start.next
    key.data,tempPrevious.data = tempPrevious.data,key.data
    return tempPrevious

def quickSortUtil(start,end):
    if start is not None and start.next is not None and start is not end:
        key = start
        pos = partition(start.next, end, key)
        quickSortUtil(start, pos)
        quickSortUtil(pos.next, end)

def quickSort(head):
    originalHead = head
    quickSortUtil(originalHead, None)
    
def generateRandomNumbersList():
    length = random.randint(1,10)
    inp = [0] * length
    for i in xrange(length):
        inp[i] = random.randint(1,100)
    return inp
    

if __name__ == '__main__':
    s = getList([90,20,59])
    printList(s)
    quickSort(s)
    printList(s)
    
    #===========================================================================
    # for i in xrange(10):
    #     sample = getList(generateRandomNumbersList())
    #     printList(sample)
    #     quickSort(sample)
    #     printList(sample)
    #===========================================================================
