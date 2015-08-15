import random
class Node :
    def __init__(self,data,next):
        self.data = data
        self.next = next

def getList(inp):
    head = None
    tail = None
    for e in inp:
        if head is None:
            head = Node(e,None)
            tail = head
        else:
            tail.next = Node(e,None)
            tail = tail.next
            
    return head

def printList(head):
    while head is not None:
        print head.data, 
        head = head.next
    print
    
def printReverse(head):
    if head == None:
        return
    else:
        printReverse(head.next)
        print head.data
        
def printAlternate(head):
    if head == None:
        return
    else:
        print head.data
        if head.next is not None:
            printAlternate(head.next.next)
            print head.next.data
            


def split(head):
    if head.next is None:
        f = head
        s = None
    else:
        slowPrevious = None
        slow = fast = head
        while fast is not None and fast.next is not None:
            slowPrevious = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        
        f = head
        s = slow
        slowPrevious.next = None
    
    return (f,s)


def merge(first,second):
    originalFirst = first
    firstPrevious = None
    while first is not None and second is not None:
        if first.data < second.data:
            firstPrevious = first
            first = first.next
        else:
            temp = second.next
            second.next = first
            if firstPrevious is not None:
                firstPrevious.next = second
                firstPrevious = second
            else:
                firstPrevious = second
                originalFirst = firstPrevious
            second = temp
    
    if second is not None:
        firstPrevious.next = second
    
    return originalFirst


def mergeSort(head):
    if head is None or head.next is None:
        return head
    else:
        f,s = split(head)
        f = mergeSort(f)
        s = mergeSort(s)
        merged = merge(f,s)
        return merged


def generateRandomNumbersList():
    length = random.randint(1,10)
    inp = [0] * length
    for i in xrange(length):
        inp[i] = random.randint(1,100)
    return inp
        

if __name__ == '__main__':
    
    for i in xrange(10):
        sample = getList(generateRandomNumbersList())
        printList(sample)
        re = mergeSort(sample)
        printList(re)
    
    
    sample = getList([36,79,38,76,69,69])
    printList(sample)
    re = mergeSort(sample)
    printList(re)