class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        

def search(inorder, data, sI, eI):
    for i in xrange(sI, eI + 1):
        if inorder[i] == data:
            return i
    return -1
        
def getTreeFromInorderPreorderUtil(inorder, preorder, sI, eI):
    if sI > eI:
        return None
    elif sI == eI:
        node = Node(preorder[getTreeFromInorderPreorder.preIndex], None, None)
        getTreeFromInorderPreorder.preIndex += 1
        return node
    else:
        data = preorder[getTreeFromInorderPreorder.preIndex]
        node = Node(data, None, None)
        getTreeFromInorderPreorder.preIndex += 1
        ind = search(inorder, data, sI, eI)
        node.left = getTreeFromInorderPreorderUtil(inorder, preorder, sI, ind - 1)
        node.right = getTreeFromInorderPreorderUtil(inorder, preorder, ind + 1, eI)
        return node

def getTreeFromInorderPreorder(inorder, preorder):
    getTreeFromInorderPreorder.preIndex = 0
    root = getTreeFromInorderPreorderUtil(inorder, preorder, 0, len(inorder) - 1)
    return root

def extractLeftRightLevelOrder(levelorder,index,inorder,sI,eI):
    left = []
    right = []
    for i in xrange(index,len(levelorder)):
        found = False
        for j in xrange(sI,eI+1):
            if levelorder[i] == inorder[j]:
                left.append(inorder[j])
                found = True
                break
        if not found:
            right.append(levelorder[i])
    return left,right

def getTreeFromInorderLevelorderUtil(inorder, levelorder, sI, eI):
    if sI > eI:
        return None
    elif eI == sI:
        node = Node(levelorder[0], None, None)
        return node
    else:
        data = levelorder[0]
        node = Node(data, None, None)
        ind = search(inorder, data, sI, eI)
        left,right = extractLeftRightLevelOrder(levelorder, 1, inorder,sI,ind - 1)
        node.left = getTreeFromInorderLevelorderUtil(inorder, left, sI, ind - 1)
        node.right = getTreeFromInorderLevelorderUtil(inorder, right, ind + 1, eI)
        return node
        

def getTreeFromInorderLevelorder(inorder, levelorder):
    root = getTreeFromInorderLevelorderUtil(inorder, levelorder, 0, len(levelorder) - 1)
    return root 

def postOrderUtil(root):
    if root is not None:
        postOrderUtil(root.left)
        postOrderUtil(root.right)
        print root.data,
        
def postOrder(root):
    print "PostOrder = ",
    postOrderUtil(root)
    print 
    
if __name__ == '__main__':
    inorder = list("DBACE")
    preorder = list("ABDCE")
    levelorder = list("ABCDE")
    
    root = getTreeFromInorderPreorder(inorder, preorder)
    postOrder(root)
    
    root = getTreeFromInorderLevelorder(inorder, levelorder)
    postOrder(root)
    

    
