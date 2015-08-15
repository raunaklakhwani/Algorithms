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

    d = {}
    d[2] = [7,5]
    d[7] = [None,6]
    d[5] = [None,9]
    d[6] = [1,11]
    d[9] = [4]
    return d

def removeAllOneChildNode(root):
    if root is None:
        return None
    else:
        left = removeAllOneChildNode(root.left)
        right = removeAllOneChildNode(root.right)
        root.left = left
        root.right = right
        if (left is not None and right is not None) or (left is None and right is None):
            return root
        else:
            return left if left is not None else right

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 2)
    inorder(root)
    print 
    print "____________________________"
    root = removeAllOneChildNode(root)
    inorder(root)
    