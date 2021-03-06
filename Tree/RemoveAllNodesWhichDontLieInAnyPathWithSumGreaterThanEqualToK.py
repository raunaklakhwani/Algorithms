# URL : http://www.geeksforgeeks.org/remove-all-nodes-which-lie-on-a-path-having-sum-less-than-k/
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
    
def inOrderUtil(root):
    if root is not None:
        inOrderUtil(root.left)
        print root.data,
        inOrderUtil(root.right)
        
def inOrder(root):
    print "InOrder = ",
    inOrderUtil(root)
    print 


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
    d[1] = [2,3]
    d[2] = [4,5]
    d[3] = [6,7]
    d[4] = [8,9]
    d[5] = [12]
    d[7] = [10]
    d[10] = [None,11]
    d[9] = [13,14]
    d[14] = [15]
    return d

def removeAllNodesUtil(root,K,l,parent):
    if root is not None:
        l.append(root.data)
        root.left = removeAllNodesUtil(root.left, K,l,root)
        root.right = removeAllNodesUtil(root.right, K,l,root)
        l.pop()
        
        if root.left is None and root.right is None:
            if root.data + sum(l) < K:
                if parent:
                    if parent.left == root:
                        parent.left = None
                    else:
                        parent.right = None
                    return None
                else:
                    return None
            else:
                return root
        
        return root

def removeAllNodes(root,K):
    if root is not None:
        return removeAllNodesUtil(root, K,[],None)

        

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    inOrder(root)
    root = removeAllNodes(root, 45)
    inOrder(root)
    
    
    
