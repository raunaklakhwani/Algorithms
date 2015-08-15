class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        


def getList(li):
    head = tail = None
    for i in li:
        if head is None:
            head = tail = Node(i, None)
        else:
            tail.next = Node(i, None)
            tail = tail.next
    return head

def printList(head):
    temp = head
    while temp is not None:
        print temp.data,
        temp = temp.next
        
    print 

def getDay(head):
    deleted = False
    temp = head
    preDelete = None
    deletedFlag = False
    while temp is not None:
        if temp.next is not None and temp.data < temp.next.data:
            if not deletedFlag:
                deleted = True
                deletedFlag = True
                preDelete = temp
        else:
            if deletedFlag:
                preDelete.next = temp.next
                deletedFlag = False
                preDelete = None
        temp = temp.next
    # printList(head)
    return deleted

def getData(p):
    print 
    maxa = 0
    stack = []
    for i in xrange(len(p)):
        if len(stack) == 0:
            stack.append((p[i], 0))
        else:
            temp = stack[-1]
            if p[i] >= temp[0]:
                sc = 1
                maxa = max(maxa, sc)
                stack.append((p[i], sc))
            else:
                v = stack[-1]
                pr = v[1]
                while len(stack) and v[0] > p[i]:
                    stack.pop()
                    if len(stack) == 0:
                        break
                    pr = max(pr, v[1])
                    v = stack[-1]
                
                if len(stack) == 0:
                    stack.append((p[i], 0))
                else:
                    stack.append((p[i], pr + 1))
                    maxa = max(maxa, pr + 1)
        print stack, maxa
                    
    return maxa
                    
            
            
    
if __name__ == '__main__':
    N = 7
    p = [6, 5, 8, 4, 7, 10 , 9]
    head = getList(p)
    # printList(head)
    
    count = 0
    while getDay(head):
        count += 1
    print count
    
    print getData(p)
        
