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
    

def reverseListPairWise(head):
    if head is not None and head.next is not None:
        first = head
        second = head.next
        third = head.next.next
        
        #head = head.next.next
        
        
        second.next = first
        first.next = reverseListPairWise(third)
        head = second
        #printList(head)
        
        
    return head
    
    

if __name__ == '__main__':
    first = getList([1,3,5,7,9,10])
    printList(first)
    rev = reverseListPairWise(first)
    printList(rev)
    
    