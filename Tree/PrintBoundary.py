#URL : http://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/
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
    d[20] = [8, 22]
    d[8] = [4, 12]
    d[12] = [10, 14]
    d[22] = [None, 25]
    d[25] = [18]
    d[18] = [None,17]
    d[4] = [None,50]
    d[50] = [100]
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

def goToLeafLeft(root):
    if root is None or (root.left is None and root.right is None):
        return True
    elif root.left:
        print root.data,
        goToLeafLeft(root.left)
    elif root.right:
        print root.data,
        goToLeafLeft(root.right)
    else:
        return False
        
def goToLeafRight(root):
    if root is None or (root.left is None and root.right is None):
        return True
    elif root.right:
        goToLeafRight(root.right)
        print root.data,
    elif root.left:
        goToLeafRight(root.left)
        print root.data,
    else:
        return False
        

def printLeftBoundary(root):
    goToLeafLeft(root)
            
def printLeaves(root):
    if root:
        printLeaves(root.left)
        if root.left is None and root.right is None:
            print root.data,
        printLeaves(root.right)
        

def printRightBoundary(root):
    goToLeafRight(root)    
    

def printBoundary(root):
    printLeftBoundary(root)
    printLeaves(root)
    if root.right is not None:
        printRightBoundary(root.right) 

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 20)
    inOrder(root)
    print
    printBoundary(root)
    
    
