#URL : http://www.geeksforgeeks.org/avl-tree-set-2-deletion/ for deletion
from _collections import deque
class Node:
    
    def __init__(self, data, left, right, height):
        self.data = data
        self.left = left
        self.right = right
        self.height = height


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)
        
def getHeight(node):
    if node is not None:
        return node.height
    else:
        return 0

def LLRotation(W):
    X = W.left
    W.left = X.right
    X.right = W
    W.height = max(getHeight(W.left), getHeight(W.right)) + 1
    X.height = max(W.height, getHeight(X.left)) + 1
    return X

def RRRotation(W):
    X = W.right
    W.right = X.left
    X.left = W
    W.height = max(getHeight(W.left), getHeight(W.right)) + 1
    X.height = max(W.height, getHeight(X.right)) + 1
    return X

def LRRotation(W):
    W.left = RRRotation(W.left)
    return LLRotation(W)

def RLRotation(W):
    W.right = LLRotation(W.right)
    return RRRotation(W)
 
def insertAVLNode(root, data):
    if root is None:
        return Node(data, None, None, 1)
    elif data <= root.data:
        root.left = insertAVLNode(root.left, data)
    else:
        root.right = insertAVLNode(root.right, data)
    
    if getHeight(root.left) - getHeight(root.right) > 1:
        if data <= root.left.data:
            root = LLRotation(root)
        else:
            root = LRRotation(root)
    elif getHeight(root.right) - getHeight(root.left) > 1:
        if data <= root.right.data:
            root = RLRotation(root)
        else:
            root = RRRotation(root)
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    return root
 
def getAvlTree(inp):
    root = None
    for i in inp:
        root = insertAVLNode(root, i)
        inorder(root)
        print 
        print root.height
        print "_____________________"
    return root

def levelOrder(root):
    if root is not None:
        q = deque([root, None])
        while len(q):
            item = q.popleft()
            if item:
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
                print item.data,
            else:
                print
                if len(q):
                    q.append(None)
                else:
                    break
        
def getBalanceFactor(root):
    return getHeight(root.left) - getHeight(root.right)
            

def deleteNodeUtil(root, data):
    '''
    The idea is to delete the node as you delete in BST and after deleting see that the parent node is imbalanced or not.
    In case it is imbalanced, then check to see whether it is due to LL,LR,RL,or RR. just do that and go upwards while checking.
    '''
    if root is not None:
        if data < root.data:
            root.left = deleteNodeUtil(root.left, data)
        elif data > root.data:
            root.right = deleteNodeUtil(root.right, data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            parentLeft = None
            left = root.left
            while left.right is not None:
                parentLeft = left
                left = left.right
            root.data = left.data
            if parentLeft is not None:
                parentLeft.right = deleteNodeUtil(left, left.data)
            else:
                root.left = deleteNodeUtil(left, left.data)
        
        root.height = max(getHeight(root.left), getHeight(root.right)) + 1
        
        balanceFactor = getBalanceFactor(root)
        if balanceFactor > 1:
            leftBalanceFactor = getBalanceFactor(root.left)
            if leftBalanceFactor >= 0:
                root = LLRotation(root)
                return root
            else:
                root = LRRotation(root)
                return root
        
        if balanceFactor < -1:
            rightBalanceFactor = getBalanceFactor(root.right)
            if rightBalanceFactor <= 0:
                root = RRRotation(root)
                return root
            else:
                root = RLRotation(root)
                return root
        
        return root
            
            
                
            
        
    else:
        return None

def deleteNode(root, data):
    root = deleteNodeUtil(root, data)
    return root

if __name__ == '__main__':
    inp = [3, 2, 1, 4, 5, 6, 7, 16, 15, 14]
    root = getAvlTree(inp)
    print "___________________"
    levelOrder(root)
    print "___________________"
    
    #===========================================================================
    # root = deleteNode(root, 4)
    # levelOrder(root)
    # print "___________________"
    # root = deleteNode(root, 5)
    # levelOrder(root)
    # print "___________________"
    # root = deleteNode(root, 15)
    # levelOrder(root)
    # print "___________________"
    #===========================================================================
    
    while root is not None:
        root = deleteNode(root, root.data)
        levelOrder(root)
        print "___________________"
    
    
    
    
    
    
