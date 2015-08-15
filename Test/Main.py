

def merge(a,b):
    result = None
    resultEnd = None
    while a is not None and b is not None:
        if a.data < b.data:
            if resultEnd is None:
                resultEnd = Node(a.data,None,None)
                result = resultEnd
            else:
                resultEnd.down = Node(a.data,None,None)
                resultEnd = resultEnd.down
                
            a = a.down
        else:
            if resultEnd is None:
                resultEnd = Node(b.data,None,None)
                result = resultEnd
            else:
                resultEnd.down = Node(b.data,None,None)
                resultEnd = resultEnd.down
            b = b.down
    
    if a is None:
        while b is not None:
            resultEnd.down = Node(b.data,None,None)
            resultEnd = resultEnd.down
            b = b.down
    if b is None:
        while a is not None:
            resultEnd.down = Node(a.data,None,None)
            resultEnd = resultEnd.down
            a = a.down
    return result
        


class Node:
    def __init__(self,data,next,down):
        self.data = data
        self.next = next
        self.down = down
        
head = Node(5,None,Node(7,None,Node(8,None,Node(30,None,None))))
head.next = Node(10,None,Node(20,None,None))
head.next.next = Node(19,None,Node(22,None,Node(50,None,None)))
head.next.next.next = Node(28,None,Node(35,None,Node(40,None,Node(45,None,None))))


count = 0
temp = head
while temp is not None:
    count += 1
    temp = temp.next

result = head 
temp = head  
for i in xrange(count - 1):
    temp = temp.next
    result = merge(result,temp)
    
#print result
while result is not None:
    print result.data, 
    result = result.down
    



        
            
            
                

