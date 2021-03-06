from _collections import deque
class Node:
    
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def getTreeDict():
    #===========================================================================
    # d = {}
    # d[1] = [2,3]
    # d[2] = [4,5]
    # d[3] = [6]
    # d[4] = [7,8]
    # return d
    #===========================================================================

    d = {}
    d[1] = [2,3]
    d[2] = [4,5]
    d[4] = [7]
    return d

def constructTree(d, key):
    if d.get(key) is None:
        return Node(key, None, None)
    else:
        root = Node(key, None, None)
        child = d[key]
        if len(child) == 1:
            if child[0] is not None:
                root.left = constructTree(d, child[0])
        elif len(child) == 2:
            if child[0] is not None:
                root.left = constructTree(d, child[0])
            if child[1] is not None:
                root.right = constructTree(d, child[1])
        return root
    
def inOrderUtil(root):
    if root is not None:
        inOrderUtil(root.left)
        print root.data,
        inOrderUtil(root.right)
        
def inOrder(root):
    print "InOrder = ",
    inOrderUtil(root)
    print 

def getAncestorsUtil(root,data,level,l):
    if root is not None:
        if root.data == data:
            getAncestors.level = level
        else:
            getAncestorsUtil(root.left, data,level + 1,l)
            if getAncestors.level is None:
                getAncestorsUtil(root.right, data,level + 1,l)
            if getAncestors.level is not None:
                if level < getAncestors.level:
                    l.append(root.data)
            
    
def getAncestors(root,data):
    l = []
    getAncestors.level = None
    getAncestorsUtil(root, data, 0, l)
    return l

def getAncestorsRecursive(root,data,l):
    if root is not None:
        if root.data != data:
            l.append(root.data)
            getAncestorsRecursive(root.left, data,l)
            l.pop()
            l.append(root.data)
            getAncestorsRecursive(root.right, data,l)
            l.pop()
            
            
        else:
            print l
            
def getAncestorRecursiveReverse(root,data,l):
    if root is not None:
        if root.data != data:
            l.appendleft(root.data)
            getAncestorRecursiveReverse(root.left, data,l)
            l.popleft()
            l.appendleft(root.data)
            getAncestorRecursiveReverse(root.right, data,l)
            l.popleft()
        else:
            print l
    

def printStack(s):
    for i in s:
        print i.data,
         
def getAncestorIterative(root,data):
    '''
    The idea is to traverse the tree in the post order and whenever you find the node, whatever in the stack is the answer.
    '''
    if root is not None:
        s = []
        temp = root
        done = False
        while True:
            while temp is not None:
                s.append(temp)
                temp = temp.left
            
            if not len(s):
                break
            
            if s[-1].right:
                temp = s[-1].right
            else:
                item = s.pop()
                if item.data == data:
                    done = True
                    printStack(s)
                    break
                #print item.data,
                if item != s[-1].right:
                    temp = s[-1].right
                else:
                    while len(s) and item == s[-1].right:
                        item = s.pop()
                        if item.data == data:
                            done = True
                            printStack(s)
                            break
                        #print item.data,
                        if not len(s):
                            break
                     
                    if done:
                        break   
                    if len(s):
                        temp = s[-1].right
                    else:
                        break
                        
                        
                    
                
                
               
    print
            
    

            
if __name__ == '__main__':
    N = 7
    root = constructTree(getTreeDict(), 1)
    inOrder(root)
    print getAncestors(root, N)
    l = []
    print "____________"
    getAncestorsRecursive(root, N,l)
    getAncestorRecursiveReverse(root, N, deque([]))
    
    getAncestorIterative(root, N)
