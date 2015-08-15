class Node:
    def __init__(self, data, previous, next):
        self.data = data
        self.previous = previous
        self.next = next

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

def inorder(root):
    if root is not None:
        inorder(root.previous)
        print root.data,
        inorder(root.next)
        
def printList(head):
    while head is not None:
        print head.data,
        head = head.next
    print

def getCount(head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    return count
    
def getBSTUtil(start, end):
    if start > end:
        return None
    elif start == end:
        temp = getBST.head
        getBST.head = getBST.head.next
        temp.previous = temp.next = None
        return temp
    mid = start + (end - start) / 2 
    left = getBSTUtil(start, mid - 1)
    currentHead = getBST.head
    currentHead.previous = left
    getBST.head = getBST.head.next
    right = getBSTUtil(mid + 1, end)
    currentHead.next = right
    return currentHead

def getBST(head):
    getBST.head = head
    count = getCount(head)
    root = getBSTUtil(0, count - 1)
    return root
    
if __name__ == '__main__':
    head = getList([-5, 1, 3, 5, 6, 7, 10, 12, 20])
    printList(head) 
    print "______________________"
    root = getBST(head)
    inorder(root)
    
