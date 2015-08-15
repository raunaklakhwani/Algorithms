class Node :
    def __init__(self,data,next,child):
        self.data = data
        self.next = next
        self.child = None

def getList(inp):
    head = None
    tail = None
    for e in inp:
        if head is None:
            head = Node(e,None,None)
            tail = head
        else:
            tail.next = Node(e,None,None)
            tail = tail.next
            
    return head

def printList(head):
    while head is not None:
        print head.data, 
        head = head.next
    print

def createList():
    fl = getList([10,5,12,7,11])
    sl1 = getList([4,20,13])
    sl2 = getList([17,6])
    tl1 = getList([2])
    tl2 = getList([16])
    tl3 = getList([9,8])
    fl1 = getList([3])
    fl2 = getList([19,15])
    
    fl.child = sl1
    fl.next.next.next.child = sl2
    
    sl1.next.child = tl1
    sl1.next.next.child = tl2
    
    sl2.child = tl3
    
    tl2.child = fl1
    tl3.child = fl2
    
    return fl

def flattenList(head):
    originalHead = head
    while head is not None and head.next is not None:
        head = head.next
    tail = head
    
    temp = originalHead
    while temp is not None:
        if temp.child is not None:
            tail.next = temp.child
            while tail.next is not None:
                tail = tail.next
        temp = temp.next
        
    return originalHead
            
    
        
    
    
    
if __name__ == '__main__':
    head = createList()
    head = flattenList(head)
    printList(head)
    