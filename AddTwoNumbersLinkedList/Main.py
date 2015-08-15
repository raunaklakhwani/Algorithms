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
    
def getLength(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def getReverse(head):
    if head is None:
        return
    for i in getReverse(head.next):
        yield i
    yield head.data

def getSum(f, s):
    sumListHead = None
    rf = getReverse(f)
    rs = getReverse(s)
    carry = 0
    while True:
        digits = 0
        try:
            i = next(rf)
        except StopIteration:
            i = 0
            digits += 1
            
        try:
            j = next(rs)
        except StopIteration:
            j = 0
            digits += 1
            
        if digits == 2:
            break
        su = i + j + carry
        carry = su / 10
        su = su % 10
        
        node = Node(su, None, None)
        if sumListHead is None:
            sumListHead = node
        else:
            node.next = sumListHead
            sumListHead = node
    if carry:
        node = Node(carry,None,None)
        node.next = sumListHead
        sumListHead = node
        
    return sumListHead

if __name__ == '__main__':
    f = getList([5, 6, 3])
    s = getList([8, 4, 2])
    l = getSum(f, s)
    printList(l)
    
    
