N = 81
M = 5

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

def advanceHead(head,M):
    i = 0
    temp = head
    tempPrevious = None
    while i < M-1:
        tempPrevious = temp
        temp = temp.next
        i += 1
    return (tempPrevious,temp)
        
def getJosephusWinner(head):
    temp = head
    while temp.next != temp:
        tempPrevious,temp = advanceHead(temp,M)
        #Delete temp node
        tempPrevious.next = temp.next
        temp.next = None
        print temp.data,
        temp = tempPrevious.next
    print     
    return temp.data
        
        
        

if __name__ == '__main__':
    f = getCircularList(range(1,N+1))
    printCircularList(f)
    print getJosephusWinner(f)
    
    
    