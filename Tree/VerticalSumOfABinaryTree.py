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
    d[1] = [2, 3]
    d[2] = [4, 5]
    d[3] = [None, 6]
    d[4] = [7, 8]
    d[6] = [None,10]
    return d


def verticalSumBinaryTreeUtil(root,vertical,d):
    if root is not None:
        d.setdefault(vertical,0)
        d[vertical] += root.data
        verticalSumBinaryTreeUtil(root.left, vertical - 1, d)
        verticalSumBinaryTreeUtil(root.right, vertical + 1, d)
    

def verticalSumBinaryTree(root):
    d = {}
    verticalSumBinaryTreeUtil(root,0,d)
    return d

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    print verticalSumBinaryTree(root)
    
    
    
    
    
    
    
    
