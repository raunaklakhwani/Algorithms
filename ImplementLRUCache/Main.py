#http://www.geeksforgeeks.org/implement-lru-cache/
numOfPages = 10
cacheSize = 4


class Node:
    def __init__(self,data,previous,next):
        self.data = data
        self.previous = previous
        self.next = next



class Queue:
    def __init__(self,front,rear):
        self.front = front
        self.rear = rear
        self.length = 0
        
    def getLength(self):
        return self.length
    
    def isFull(self):
        return self.length == cacheSize
    
    def insert(self,num):
        if self.length < cacheSize:
            self.length += 1
            if self.front is None:
                self.front = self.rear = Node(num,None,None)
            else:
                temp = Node(num,None,self.front)
                self.front.previous = temp
                self.front = temp
        else:
            temp = self.rear.previous
            temp.next = None
            self.rear.previous = None
            self.rear = temp
            temp = Node(num,None,self.front)
            self.front.previous = temp
            self.front = temp
            
        return self.front
            
    def moveNodeToFront(self,node):
        if self.front is node:
            return 
        else:
            pre = node.previous
            next = node.next
            pre.next = next
            self.rear = pre
            if next is not None:
                next.pre = pre
            self.front.previous = node
            node.next = self.front
            node.previous = None
            self.front = node     
    
    
        
class LRUCache:
    def __init__(self,q,hash):
        self.q = q
        self.hash = hash
        
    def referencePageNumber(self,pageNum):
        if self.hash[pageNum] is None:
            node = self.q.insert(pageNum)
            self.hash[pageNum] = node
        else:
            node = self.hash[pageNum]
            self.q.moveNodeToFront(node)
            
    def printQ(self):
        temp = self.q.front
        while temp is not None:
            print temp.data,
            temp = temp.next
        print
        
        print "rear", self.q.rear.data
        print "front", self.q.front.data
        
    def printHash(self):
        for i in xrange(numOfPages):
            if self.hash[i] is not None:
                print i, " --> ", self.hash[i].data
            else:
                print i, " --> ", None
                
            
        
        


if __name__ == '__main__':
    cache = LRUCache(Queue(None,None),[None]*numOfPages)
    
    references = [1,2,3,1,4,5]
    for i in references:
        cache.referencePageNumber(i)
        cache.printQ()
        cache.printHash()
        print "___________________"
    #===========================================================================
    # cache.referencePageNumber(1)
    # cache.referencePageNumber(2)
    # cache.referencePageNumber(3)
    # cache.referencePageNumber(1)
    # cache.referencePageNumber(4)
    # cache.referencePageNumber(5)
    #===========================================================================
    
    
    
    