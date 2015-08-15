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
    
def alternatingSplit(head):
    s = f = None
    if head is None:
        return (None,None)
    elif head.next is None:
        return (head,None)
    else:
        f = head
        s = head.next
        a,b = alternatingSplit(head.next.next)
        f.next = a
        s.next = b
        return (f,s)
    
    
if __name__ == '__main__':
    f = getList(list("01010101010"))
    s = getList(list("010101010101"))
    #printList(f)
    #printList(s)
    
    a,b = alternatingSplit(f)
    printList(a)
    printList(b)
    
    a,b = alternatingSplit(s)
    printList(a)
    printList(b)
    
    