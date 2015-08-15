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
    d[10] = [7,15]
    d[7] = [None,9]
    d[15] = [None,11]
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

def isFoldableUtil(left,right):
    if left is None and right is None:
        return True
    elif left is not None and right is not None:
        return isFoldableUtil(left.left, right.right) and isFoldableUtil(left.right, right.left)
    return False

def isFoldable(root):
    if root is None:
        return True
    else:
        return isFoldableUtil(root.left, root.right)
                    
            
if __name__ == '__main__':
    root = constructTree(getTreeDict(), 10)
    inOrder(root)
    print isFoldable(root)
    