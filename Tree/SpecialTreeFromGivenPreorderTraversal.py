#URL : http://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/

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
    d[50] = [7, 2]
    d[7] = [3, 5]
    d[2] = [1, 30]
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
    
def getSpecialTreeUtil(pre, preLN):
    
    if getSpecialTree.index < len(pre):
        if preLN[getSpecialTree.index] == "L":
            #getSpecialTree.index += 1
            return Node(pre[getSpecialTree.index], None, None)
        else:
            node = Node(pre[getSpecialTree.index], None, None)
            getSpecialTree.index += 1
            node.left = getSpecialTreeUtil(pre, preLN)
            getSpecialTree.index += 1
            node.right = getSpecialTreeUtil(pre, preLN)
            return node
    

def getSpecialTree(pre, preLN):
    getSpecialTree.index = 0
    root = getSpecialTreeUtil(pre, preLN)
    return root

if __name__ == '__main__':
    pre = [10, 30, 20, 5, 15]
    preLN = ['N', 'N', 'L', 'L', 'L']
    root = getSpecialTree(pre, preLN)
    inOrder(root)
