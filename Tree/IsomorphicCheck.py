#URL : www.geeksforgeeks.org/tree-isomorphism-problem/
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
    d[1] = [2, 3]
    d[2] = [4, 5]
    d[5] = [7, 8]
    d[3] = [6]
    return d

def getTreeDict1():
    #===========================================================================
    # d = {}
    # d[1] = [2,3]
    # d[2] = [4,5]
    # d[3] = [6]
    # d[4] = [7,8]
    # return d
    #===========================================================================

    d = {}
    d[1] = [3, 2]
    d[3] = [None, 6]
    d[2] = [4, 5]
    d[5] = [8, 7]
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

def isIsomorphic(root,root1):
    if root and root1:
        if root.data == root1.data:
            if isIsomorphic(root.left, root1.left):
                return isIsomorphic(root.right, root1.right)
            elif isIsomorphic(root.left, root1.right):
                return isIsomorphic(root.right, root1.left)
            else:
                return False
        else:
            return False
    if root is None and root1 is None:
        return True
    return False

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    root1 = constructTree(getTreeDict1(), 1)
    inOrder(root)
    inOrder(root1)
    print isIsomorphic(root, root1)
    
