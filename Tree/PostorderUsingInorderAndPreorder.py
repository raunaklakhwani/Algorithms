# URL : http://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/
from _collections import deque

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def getTreeUsingInorderPreorderUtil(inorder, preorder, ins, ine, pres):
    if ins > ine:
        return None
    elif ins == ine:
        return Node(inorder[ins], None, None)
    else:
        node = Node(preorder[pres], None, None)
        index = inorder.index(preorder[pres])
        node.left = getTreeUsingInorderPreorderUtil(inorder, preorder, ins, index - 1, pres + 1)
        node.right = getTreeUsingInorderPreorderUtil(inorder, preorder, index + 1, ine, pres + index - ins + 1)
        return node
        

def getTreeUsingInorderPreorder(inorder, preorder):
    if len(inorder):
        return getTreeUsingInorderPreorderUtil(inorder, preorder, 0, len(inorder) - 1, 0)
        

def getPostorderUsingInorderPreorderUtil(inorder, preorder, ins, ine, pres):
    if ins > ine:
        return deque([])
    elif ins == ine:
        return deque([inorder[ins]])
    else:
        d = deque([preorder[pres]])
        index = inorder.index(preorder[pres])
        left = getPostorderUsingInorderPreorderUtil(inorder, preorder, ins, index - 1, pres + 1)
        right = getPostorderUsingInorderPreorderUtil(inorder, preorder, index + 1, ine, pres + index - ins + 1)
        
        while len(right):
            d.appendleft(right.pop())
            
        while len(left):
            d.appendleft(left.pop())
        #d.extendleft(right)
        #d.extendleft(left)
        return d

index = 0    
def recurse(inorder,preorder,s,e):
    global index
    if s > e:
        return ""
    elif s == e:
        element = preorder[index]
        index += 1
        return str(element)
    else:
        element = preorder[index]
        mid = inorder.index(element)
        index += 1
        left = recurse(inorder,preorder,s,mid - 1)
        right = recurse(inorder, preorder, mid + 1, e)
        #print left,right,element
        s1 = left + right + str(element)
        return s1
        
        
        

def getPostorderUsingInorderPreorder(inorder, preorder):
    if len(inorder):
        return getPostorderUsingInorderPreorderUtil(inorder, preorder, 0, len(inorder) - 1, 0)

def postTraversal(root):
    if root is not None:
        postTraversal(root.left)
        postTraversal(root.right)
        print root.data,


if __name__ == '__main__':
    inorder = [4, 2, 5, 1, 3, 6]
    preorder = [1, 2, 4, 5, 3, 6]
    root = getTreeUsingInorderPreorder(inorder, preorder)
    postTraversal(root)
    print 
    print getPostorderUsingInorderPreorder(inorder, preorder)
    print recurse(inorder, preorder, 0, len(preorder) - 1)
    
    
