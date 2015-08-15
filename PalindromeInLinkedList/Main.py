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
    
def checkPalindrome(head):
    isPalindrome = True
    if head is None or head.next is None:
        isPalindrome = True
    else:
        fast = slow = head
        slowPrevious = None
        while fast is not None:
            slowPrevious = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
                
        first = head
        last = slow
        
        rev = reverseList(last)
        revCopy = rev
        while rev is not None:
            if first.data != rev.data:
                isPalindrome = False
                break
            else:
                first = first.next
                rev = rev.next
                
        reverseList(revCopy)
        return isPalindrome
        
def reverseList(head):
    f = None
    t = head
    while t is not None:
        n = t.next
        t.next = f
        f = t
        t = n
    return f

    

    
if __name__ == '__main__':
    f = getList(list("abcdcba"))
    s = getList(list("abcddcba"))
    t = getList(list("abcdcbd"))
    ft = getList(list("abcddcaa"))
    
    print checkPalindrome(f)
    print checkPalindrome(s)
    print checkPalindrome(t)
    print checkPalindrome(ft)
    print "hello"
    print printList(f)
    