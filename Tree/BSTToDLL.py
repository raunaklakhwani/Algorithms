from _collections import deque
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

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
    
def getTreeDict():
    #===========================================================================
    # d = {}
    # d[1] = [2,3]
    # d[2] = [4,5]
    # d[3] = [6]
    # d[4] = [7,8]
    # return d
    #===========================================================================

    #===========================================================================
    # d = {}
    # d[1] = [2, 3]
    # d[2] = [4, 5]
    # d[3] = [6, 7]
    # d[4] = [8, 9]
    # d[6] = [10, 11]
    # return d
    #===========================================================================

    #===========================================================================
    # d = {}
    # d[1] = [2]
    # d[2] = [3,4]
    # return d
    #===========================================================================
    
    d = {}
    d[5] = [1,7]
    d[1] = [-5,3]
    d[7] = [6,12]
    d[12] = [10,20]
    return d


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)

def getDLL(root):
    if root is None:
        return (None,None)
    elif root.left is None and root.right is None:
        return (root,root)
    else:
        lh,lt = getDLL(root.left)
        rh,rt = getDLL(root.right)
        root.left = lt
        root.right = rh
        lt.right = root
        rh.left = root
        return (lh,rt)
    

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 5)
    inorder(root)
    print 
    print "______________________"
    h,t = getDLL(root)
    while h is not None:
        print h.data,
        h = h.right
    print 
    

