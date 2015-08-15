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
    d[1] = [2, 3]
    d[2] = [4, 5]
    d[3] = [None, 6]
    d[4] = [7, 8]
    d[6] = [10]
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

def preordersuccessor(root,data):
    preOrderSucc = None
    if root is not None:
        s = [root]
        while len(s):
            item = s.pop()
            if item.right:
                s.append(item.right)
            if item.left:
                s.append(item.left)
            if item.data == data:
                preOrderSucc = s.pop().data if len(s) else None
                break
            
    return preOrderSucc

def inorderSuccessor(root,data):
    inOrderSucc = None
    s = []
    found = False
    while True:
        while root is not None:
            s.append(root)
            root = root.left
        if len(s):
            item = s.pop()
            if found:
                inOrderSucc = item.data
                break
            if item.data == data:
                found = True
            if item.right:
                root = item.right
        else:
            break
    return inOrderSucc

def postOrderSuccessor(root,data):
    postOrderSucc = None
    found = False
    s = []
    while True:
        while root is not None:
            s.append(root)
            root = root.left
        
        if len(s):
            item = s[-1]
            if item.right:
                root = item.right
            else:
                item = s.pop()
                if found:
                    postOrderSucc = item.data
                if item.data == data:
                    found = True
                #print item.data,
                while len(s) and s[-1].right == item:
                    item = s.pop()
                    if found:
                        postOrderSucc = item.data
                    if item.data == data:
                        found = True
                    #print item.data,
                    
                if len(s) and s[-1].right:
                    root = s[-1].right
        else:
            break
        
    return postOrderSucc
            
            
    
    

if __name__ == '__main__':
    d = getTreeDict()
    root = constructTree(d, 1)
    print preordersuccessor(root, 6)
    print inorderSuccessor(root, 6)
    print postOrderSuccessor(root,6)
    
    