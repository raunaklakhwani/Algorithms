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
    d = {}
    d[1] = [2,3]
    d[2] = [4,5]
    d[3] = [6]
    d[4] = [7,8]
    return d

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
    
    #===========================================================================
    # d = {}
    # d[1] = [2, 3]
    # d[2] = [4]
    # return d
    #===========================================================================

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)
        
def checkWhetherTreeIsCompleteOrNot(root):
    if root is None:
        return True
    else:
        q = deque([root])
        noMoreNodes = False
        while len(q):
            item = q.popleft()
            if item.left is not None:
                if not noMoreNodes:
                    q.append(item.left)
                else:
                    return False
            else:
                noMoreNodes = True
                
            if item.right is not None:
                if not noMoreNodes:
                    q.append(item.right)
                else:
                    return False
            else:
                noMoreNodes = True
                
    return True

def countNodes(root):
    if root is None:
        return 0
    else:
        left = countNodes(root.left)
        right = countNodes(root.right)
        return left + right + 1

def checkWhetherTreeIsCompleteOrNotRecursiveUtil(root, index, count):
    if root is None:
        return True
    if index >= count:
        return False
    else:
        left = 2 * index + 1
        right = 2 * index + 2
        return checkWhetherTreeIsCompleteOrNotRecursiveUtil(root.left, left, count) and checkWhetherTreeIsCompleteOrNotRecursiveUtil(root.right, right, count)

def checkWhetherTreeIsCompleteOrNotRecursive(root):
    count = countNodes(root)
    return checkWhetherTreeIsCompleteOrNotRecursiveUtil(root,0,count)
    

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    inorder(root)
    print 
    print "____________________________"
    print checkWhetherTreeIsCompleteOrNot(root)
    print "____________________________"
    print checkWhetherTreeIsCompleteOrNotRecursive(root)
    
    
    
