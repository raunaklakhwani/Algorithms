# http://www.geeksforgeeks.org/maximum-sum-linked-list-two-sorted-linked-lists-common-nodes/
class Node :
    def __init__(self, data, next):
        self.data = data
        self.next = next

def getList(inp):
    head = None
    tail = None
    for e in inp:
        if head is None:
            head = Node(e, None)
            tail = head
        else:
            tail.next = Node(e, None)
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

def getMergingPoints(f, s):
    originalF = f
    originalS = s
    sumF = 0
    sumS = 0
    mergesSumF = []
    mergesSumS = []
    mergedList = None
    mergedListTail = None
    commonPreviousF = commonPreviousS = None
    
    while f is not None and s is not None:
        if f.data == s.data:
            mergesSumF.append(sumF)
            mergesSumS.append(sumS)
            mergesSumF.append(f.data)
            mergesSumS.append(s.data)
            if mergedList is None:
                if sumF > sumS:
                    mergedList = originalF
                    mergedListTail = f
                else:
                    mergedList = originalS
                    mergedListTail = s
            else:
                if sumF>sumS:
                    mergedListTail.next = commonPreviousF.next
                    mergedListTail = f
                else:
                    mergedListTail.next = commonPreviousS.next
                    mergedListTail = s
                    
            commonPreviousF = f
            commonPreviousS = s
            sumF = 0
            sumS = 0
            f = f.next
            s = s.next
        elif f.data < s.data:
            sumF += f.data
            f = f.next
        else:
            sumS += s.data
            s = s.next
    
    
    if f is None and s is not None:
        while s is not None:
            sumS += s.data
            s = s.next
    
    if s is None and f is not None:
        while f is not None:
            sumF += f.data
            f = f.next
            
    if sumF>sumS:
        mergedListTail.next = commonPreviousF.next
        mergedListTail = f
    else:
        mergedListTail.next = commonPreviousS.next
        mergedListTail = s
        
    return mergedList
        
    
    #===========================================================================
    # if f is None:
    #     mergesSumF.append(sumF)
    # elif s is None:
    #     mergesSumS.append(sumS)
    # 
    # run = False
    # while f is not None:
    #     run = True
    #     sumF += f.data
    #     f = f.next
    # if run:
    #     mergesSumF.append(sumF)
    #  
    # run = False    
    # while s is not None:
    #     run = True
    #     sumS += s.data
    #     s = s.next
    # if run:
    #     mergesSumS.append(sumS)
    #     
    # 
    # 
    #     
    #     
    #     
    #         
    # print mergesSumF
    # print mergesSumS
    #===========================================================================
            
            
    
    #===========================================================================
    # while f is not None:
    #     if f.data == s.data:
    #         mergesSumF.append(sumF)
    #         mergesSumS.append(sumF)
    #         sumF = 0
    #         sumS = 0
    #     else:
    #         sumF += f.data
    #         sumS += s.data
    #         
    #         
    #     s = s.next
    #     f = f.next
    # print mergesSumF
    # print mergesSumS
    #===========================================================================
    
if __name__ == '__main__':
    f = getList([1, 3, 30, 90, 120, 240, 511])
    s = getList([0, 3, 12, 32, 90, 125, 240, 249])
    printList(f)
    printList(s)
    l = getMergingPoints(f, s)
    printList(l)
    
