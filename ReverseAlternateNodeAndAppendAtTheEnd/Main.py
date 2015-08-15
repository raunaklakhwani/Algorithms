#http://www.geeksforgeeks.org/given-linked-list-reverse-alternate-nodes-append-end/

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


def reverseAlternateNodeAndAppendAtTheEnd(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        temp = reverseAlternateNodeAndAppendAtTheEnd(head.next.next)
        headNext = head.next
        headNext.next = None
        head.next = temp
        t = head
        while t.next is not None:
            t = t.next
        t.next = headNext
        
    return head


def reverseAlternateNodeAndAppendAtTheEnd1(head):
    if head is None:
        return (None,None)
    elif head.next is None:
        return (head,None)
    elif head.next.next is None:
        return (head,head.next)
    else:
        temp,tail = reverseAlternateNodeAndAppendAtTheEnd1(head.next.next)
        headNext = head.next
        headNext.next = None
        head.next = temp
        tail.next = headNext
        tail = headNext
    return (head,tail)

if __name__ == '__main__':
    s = getList([1,2,3,4,5,6])
    printList(s)
    s,t = reverseAlternateNodeAndAppendAtTheEnd1(s)
    printList(s)