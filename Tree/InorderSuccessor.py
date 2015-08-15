class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None

def constructTree(d, key):
    if d.get(key) is None:
        return Node(key, None, None)
    else:
        root = Node(key, None, None)
        child = d[key]
        if len(child) == 1:
            if child[0] is not None:
                root.left = constructTree(d, child[0])
                if root.left is not None:
                    root.left.parent = root
        elif len(child) == 2:
            if child[0] is not None:
                root.left = constructTree(d, child[0])
                if root.left is not None:
                    root.left.parent = root
            if child[1] is not None:
                root.right = constructTree(d, child[1])
                if root.right is not None:
                    root.right.parent = root
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
    d[6] = [None, 10]
    return d

def search(root, data):
    if root is None:
        return None
    elif root.data == data:
        return root
    else:
        return search(root.left, data) or search(root.right, data)
    

def getInorderSuccessor(root, data):
    node = search(root, data)
    if node is None:
        return node
    else:
        if node.right is not None:
            left = node.right
            while left.left is not None:
                left = left.left
            return left
        elif node.parent and node.parent.left == node:
            return node.parent
        else:
            temp = node
            parent = node.parent
            while parent and parent.right == temp:
                temp = parent
                parent = parent.parent
            return parent
            
            
    return None


if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    
    
    li = [7, 4, 8, 2, 5, 1, 3, 6, 10, 0]
    for i in li:
        node = getInorderSuccessor(root, i)
        if node is not None:
            print i, node.data
        else:
            print i, "No Inorder successor"
    
    
    
    
    
    
    
    
    
