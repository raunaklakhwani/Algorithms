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


def mergeListRecursive(first,second):
    third = None
    while first is not None and second is not None:
        if first.data < second.data:
            third = Node(first.data,None)
            third.next = mergeListRecursive(first.next, second)
        else:
            third = Node(second.data,None)
            third.next = mergeListRecursive(first, second.next)
        return third
    
    while first is not None:
        if third is not None:
            third.next = Node(first.data,None)
        else:
            third = Node(first.data,None)
        first = first.next
        
    while second is not None:
        if third is not None:
            third.next = Node(second.data,None)
        else:
            third = Node(second.data,None)
        second = second.next
        
    return third


def mergeListNonRecursive(first,second):
    third = None
    thirdTail = None
    while first is not None and second is not None:
        if first.data < second.data:
            if third is None:
                third = Node(first.data,None)
                thirdTail = third
            else:
                thirdTail.next = Node(first.data,None)
                thirdTail = thirdTail.next
            first = first.next
        else:
            if third is None:
                third = Node(second.data,None)
                thirdTail = third
            else:
                thirdTail.next = Node(second.data,None)
                thirdTail = thirdTail.next
            second = second.next    
    
    
    while first is not None:
        if third is not None:
            thirdTail.next = Node(first.data,None)
            thirdTail = thirdTail.next
        else:
            third = Node(first.data,None)
            thirdTail = third
        first = first.next
        
    while second is not None:
        if third is not None:
            thirdTail.next = Node(second.data,None)
            thirdTail = thirdTail.next
        else:
            third = Node(second.data,None)
            thirdTail = third
        second = second.next
        
    return third

if __name__ == '__main__':
    first = getList([1,4,6,8,9])
    second = getList([2,3,5,7,10])
    printList(first)
    printList(second)
    
    third = mergeListRecursive(first, second)
    printList(third)
    
    fourth = mergeListNonRecursive(first, second)
    printList(fourth)
    
    
    
        
    