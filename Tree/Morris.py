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


def morrisTraversal(root):
    '''
    The idea behind morris traversal is setting the inorder successor of thr nodes so that rather than using the stack they might directly jump to the next node to process.
    So whenever the node is visited, its predecessor(i.e go one left and then extreme right nodes right child is pointed to the node so that whenever it is encountered, its right 
    could be used as the successor and when it is used it is also set as null so that tree original structure is maintained.
    Time complexity is O(N) and space complexity is O(1).
    '''
    print "Morris Traversal = ",
    while root is not None:
        if root.left is None:
            print root.data,
            root = root.right
            continue
        left = root.left
        while left is not None and (left.right is not None and left.right != root):
            left = left.right
        if not left.right:
            left.right = root
            root = root.left
        else:
            temp = left.right
            left.right = None
            print temp.data,
            root = temp.right
            
    print
            
            
            

if __name__ == '__main__':
    root = constructTree(getTreeDict(), 1)
    morrisTraversal(root)