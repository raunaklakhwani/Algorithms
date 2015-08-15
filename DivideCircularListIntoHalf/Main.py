class Node :
    def __init__(self,data,next):
        self.data = data
        self.next = next

def getCircularList(inp):
    head = None
    tail = None
    for e in inp:
        if head is None:
            head = Node(e,None)
            head.next = head
            tail = head
        else:
            tail.next = Node(e,head)
            tail = tail.next
            
    return head

def printCircularList(head):
    if head is None:
        return
    else:
        originalHead = head
        while head.next is not originalHead:
            print head.data, 
            head = head.next
        print head.data
        

def divideCircularList(head):
    if head is not None:
        
        originalHead = firstForward = secondForward = head
        firstBackward = secondBackward = None
        loopRun = True
        while firstForward is not originalHead or loopRun:
            loopRun = False
            
            firstBackward = secondForward
            secondForward = secondForward.next
            
            secondBackward = firstForward
            firstForward = firstForward.next
            if firstForward is not None and firstForward is not originalHead:
                secondBackward = firstForward
                firstForward = firstForward.next
                
        firstBackward.next = firstForward
        secondBackward.next = secondForward
        return(firstForward,secondForward)
            
    else:
        return (None,None)
        
if __name__ == '__main__':
    first = getCircularList([1,2,3,4,5,6,7,8,9,10])
    second = getCircularList([1,2,3,4,5,6,7,8,9])
    
    printCircularList(first)
    printCircularList(second)
    
    f,s = divideCircularList(first)
    printCircularList(f)
    printCircularList(s)
    
    f,s = divideCircularList(second)
    printCircularList(f)
    printCircularList(s)
    
    
    