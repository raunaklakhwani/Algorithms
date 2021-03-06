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

def getKthSmallestUtil(root,K):
    if root is not None and getKthSmallest.kthElement is None:
        getKthSmallestUtil(root.left,K)
        getKthSmallest.index += 1
        if getKthSmallest.index == K:
            getKthSmallest.kthElement = root.data
            return
        getKthSmallestUtil(root.right,K)

def getKthSmallest(root,K):
    getKthSmallest.index = 0
    getKthSmallest.kthElement = None
    getKthSmallestUtil(root,K)
    return getKthSmallest.kthElement
    

def getKthSmallestUsingMorrisTraversal(root,K):
    kthLargest = None
    index = 0
    while root is not None:
        if root.left is None:
            index += 1
            if index == K:
                kthLargest = root.data
            root = root.right
            continue
        left = root.left
        while left is not None and (left.right is not None and left.right != root):
            left = left.right
        if left.right is None:
            left.right = root
            root = root.left
        else:
            temp = left.right
            index += 1
            if index == K:
                kthLargest = temp.data
            left.right = None
            root = temp.right
            
            
    return kthLargest

def getKthLargestUtil(root,K):
    if root is not None and getKthLargest.kthLargest is None:
        getKthLargestUtil(root.right, K)
        getKthLargest.index += 1
        if getKthLargest.index == K:
            getKthLargest.kthLargest = root.data
            return
        getKthLargestUtil(root.left, K)

def getKthLargest(root,K):
    getKthLargest.index = 0
    getKthLargest.kthLargest = None
    getKthLargestUtil(root, K)
    return getKthLargest.kthLargest

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 5)
    inorder(root)
    print 
    
    for i in xrange(1,10):
        print getKthSmallest(root, i),
    
    print    
    print "____________________________"
        
    for i in xrange(1,10):
        print getKthSmallestUsingMorrisTraversal(root, i),
    
    print    
    print "____________________________"
        
    for i in xrange(1,10):
        print getKthLargest(root, i),
    
    