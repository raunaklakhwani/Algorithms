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
    d[50] = [7,2]
    d[7] = [3,5]
    d[2] = [1,30]
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

def makeChildrenSumTree(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return root.data
    else:
        left = makeChildrenSumTree(root.left)
        right = makeChildrenSumTree(root.right)
        if root.data <= left + right:
            root.data = left + right
        else:
            diff = root.data - left - right
            if root.left:
                increaseNodeValue(root.left, diff)
            elif root.right:
                increaseNodeValue(root.right, diff)
        return root.data
                
            
            
def increaseNodeValue(root,diff):
    if root is not None:
        root.data += diff
        if root.left:
            increaseNodeValue(root.left, diff)
        elif root.right:
            increaseNodeValue(root.right, diff)
            
                    
            
if __name__ == '__main__':
    root = constructTree(getTreeDict(), 50)
    inOrder(root)
    makeChildrenSumTree(root)
    inOrder(root)
    