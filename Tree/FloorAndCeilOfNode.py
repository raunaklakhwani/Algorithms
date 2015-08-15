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
    
    d = {}
    d[5] = [1, 7]
    d[1] = [-5, 3]
    d[7] = [6, 12]
    d[12] = [10, 20]
    return d


def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data,
        inorder(root.right)
 
 
#===============================================================================
# def ceilOperationUtil(root,num):
#     while root is not None and ceilOperation.value is None:
#         if root.data > num:
#             ceilOperation.value = root.data
#             root = root.left
#         elif root.data < num:
#             root = root.right
#         else:
#             ceilOperation.value = root.data
#             return
#     
#     if root is None:
#         return
#     else:
#         while root is not None:
#             if num < root.data:
#                 root = root.left
#===============================================================================
        
        
def ceilOperationUtil(root, num):
    if root is not None and ceilOperation.value is None:
        ceilOperationUtil(root.left, num)
        if root.data >= num and ceilOperation.value is None:
            ceilOperation.value = root.data
        ceilOperationUtil(root.right, num)
        
def ceilOperation(root, num):
    ceilOperation.value = None
    ceilOperationUtil(root, num)
    return ceilOperation.value 


def floorOperationUtil(root, num):
    if root is not None and floorOperation.value is None:
        floorOperationUtil(root.left, num)
        if root.data <= num and floorOperation.value is None:
            floorOperation.prev = root.data
        if root.data > num and floorOperation.value is None:
            floorOperation.value = floorOperation.prev
        floorOperationUtil(root.right, num)
        
def floorOperation(root, num):
    floorOperation.value = None
    floorOperation.prev = None
    floorOperationUtil(root, num)
    if floorOperation.prev is not None:
        floorOperation.value = floorOperation.prev
    return floorOperation.value 


if __name__ == '__main__':
    root = constructTree(getTreeDict(), 5)
    inorder(root)
    print
    print "__________________________"
    floorOperation(root,1)
    for i in xrange(-6, 22):
        print i,ceilOperation(root, i),floorOperation(root, i)
        print "__________________________"
    
