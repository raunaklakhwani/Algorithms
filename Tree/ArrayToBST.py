class Node:
    
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)

def insertNode(root, data):
    if root is None:
        return Node(data, None, None)
    elif data <= root.data:
        root.left = insertNode(root.left, data)
    else:
        root.right = insertNode(root.right, data)
    return root

def deleteNodeUtil(root, data, parent):
    if root is not None:
        if data < root.data:
            root.left = deleteNodeUtil(root.left, data, root)
            return root
        elif data > root.data:
            root.right = deleteNodeUtil(root.right, data, root)
            return root
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            left = root.left
            while left.right is not None:
                left = left.right
            root.data = left.data
            root.left = left.left
            return root
    else:
        return None
            
                
                
def deleteNode(root, data):
    root = deleteNodeUtil(root, data, None)
    return root
        
def getBST(inp):
    root = None
    for i in inp:
        root = insertNode(root, i)
    return root


if __name__ == '__main__':
    inp = [3, 2, 1, 4, 5, 6, 7, 16, 15, 14, 4.5]
    root = getBST(inp)
    inorder(root)
    print
    
    while root is not None:
        root = deleteNode(root, root.data)
        inorder(root)
        print
    
    
    
    
    
    
    
    
