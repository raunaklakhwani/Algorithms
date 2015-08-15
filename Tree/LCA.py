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
    d[6] = [10]
    return d

def search(root, data):
    if root is None:
        return False
    elif root.data == data:
        return True
    else:
        return search(root.left, data) or search(root.right, data)
    


def lcautil(root, node1, node2):
    if root is None:
        return None
    elif root.data == node1 or root.data == node2:
        return root
    else:
        left = lcautil(root.left, node1, node2)
        right = lcautil(root.right, node1, node2)
        if left and right:
            return root
        else:
            return left if left else right
    
def lca(root, node1, node2):
    if search(root, node1) and search(root, node2):
        return lcautil(root, node1, node2)
    else:
        return None

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    node = lca(root, 5, 7)
    if node is not None:
        print node.data
    else:
        print "Node is not present in the tree."
    
    
    
    
    
    
    
