#URL : http://www.geeksforgeeks.org/largest-independent-set-problem/
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
    d[10] = [20, 30]
    d[20] = [40, 50]
    d[50] = [70, 80]
    d[30] = [None, 60]
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

def getLISUtil(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    elif getLIS.cache.get(root) is not None:
        return getLIS.cache[root]
    elif root.left and root.right:
        return max(1 + getLIS(root.left.left) + getLIS(root.left.right) + getLIS(root.right.left) + getLIS(root.right.right), getLIS(root.left) + getLIS(root.right))
    elif root.left:
        return max(1 + getLIS(root.left.left) + getLIS(root.left.right),getLIS(root.left))
    else:
        return max(1 + getLIS(root.right.left) + getLIS(root.right.right),getLIS(root.right))
    
def getLIS(root):
    getLIS.cache = {}
    return getLISUtil(root)
    
    
        

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 10)
    inOrder(root)
    print getLIS(root)
    
