# URL : http://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/
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
    d[20] = [8, 22]
    d[8] = [4, 12]
    d[12] = [10, 14]
    d[22] = [None, 25]
    d[25] = [18]
    d[18] = [None, 17]
    d[4] = [None, 50]
    d[50] = [100]
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
    
def inOrderUtil(root):
    if root is not None:
        inOrderUtil(root.left)
        print root.data,
        inOrderUtil(root.right)
        
def inOrder(root):
    print "InOrder = ",
    inOrderUtil(root)
    print 

index = 0        
def getTreeUsingPrePostUtil(pre, post, preStart, preEnd, postStart, postEnd):
    if postStart > postEnd:
        return None
    elif postStart == postEnd:
        return Node(post[postStart], None, None)
    else:
        node = Node(pre[preStart], None, None)
        next = pre[preStart + 1]
        index = post.index(next)
        node.left = getTreeUsingPrePostUtil(pre, post, preStart + 1, preStart + 1 + index - postStart, postStart, index)
        node.right = getTreeUsingPrePostUtil(pre, post, preStart + 1 + index - postStart + 1, preEnd, index + 1, postEnd - 1)
        return node

def getTreeUsingPrePost(pre, post):
    return getTreeUsingPrePostUtil(pre, post, 0, len(pre) - 1, 0, len(pre) - 1)
    
if __name__ == '__main__':
    pre = list("124895367")
    post = list("894526731")
    root = getTreeUsingPrePost(pre, post)
    inOrder(root)
