#https://www.hackerrank.com/challenges/array-and-simple-queries
from _collections import deque
import random 
class Node:
    def __init__(self, data, left, right, size):
        self.data = data
        self.priority = random.random()
        self.left = left
        self.right = right
        self.size = size

def getSize(root):
    if root:
        return root.size
    else:
        return 0

def updateSize(root):
    if root:
        root.size = 1 + getSize(root.left) + getSize(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print root.data,
        inorder(root.right)
     
    
def preorder(root):
    if root:
        print root.data,
        preorder(root.left)
        preorder(root.right)
     
    
def levelOrder(root):
    if root:
        q = deque([root, None])
        while len(q):
            item = q.popleft()
            if item:
                print (item.data, item.priority),
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            else:
                if len(q):
                    q.append(None)
                else:
                    break
                print
    print

def getMin(root):
    if root:
        while root and root.left :
            root = root.left
        return root.data
    
def getMax(root):
    if root:
        while root and root.right :
            root = root.right
        return root.data
    

def splitUtil(root, key, count):
    if root:
        left = right = None
        tempCount = 1 + getSize(root.left)
        if count == tempCount:
            left = root
            right = root.right
            left.right = None
            updateSize(left)
            return (left, right)
        elif count > tempCount:
            left = root
            right = splitUtil(root.right, key, count - tempCount)
            left.right = right[0]
            updateSize(left)
            return (left, right[1])
        else:
            right = root
            left = splitUtil(root.left, key, count)
            right.left = left[1]
            updateSize(right)
            return (left[0], right)
    else:
        return (None, None)
                              
    
def split(root, key):
    if root:
        return splitUtil(root, key, key)
    else:
        return (None, None)
    
def merge(left, right):
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left
    else:
        if left.priority > right.priority:
            root = left
            root.right = merge(left.right, right)
        else:
            root = right
            root.left = merge(left, right.left)
        updateSize(root)
        return root


def getTreap(li):
    root = None
    for i in li:
        root = merge(root, Node(i, None, None, 1))
    return root
        

def queryOne(root, start, end):
    a, b = split(root, end)
    c, d = split(a, start - 1)
    root = merge(c, b)
    root = merge(d, root)
    return root
    
def queryTwo(root, start, end):
    a, b = split(root, end)
    c, d = split(a, start - 1)
    root = merge(c, b)
    root = merge(root, d)
    return root
    
def getOutput(root):
    print abs(getMax(root) - getMin(root))
    inorder(root)
    print
    
if __name__ == '__main__':
    N, M = 8, 4
    li = xrange(1, 9)
    root = getTreap(li)
    #===========================================================================
    # levelOrder(root)
    # inorder(root)
    # print
    # preorder(root)
    #===========================================================================
    
    li1 = [(1, 2, 4), (2, 3, 5), (1, 4, 7), (2, 1, 4)]
    for j in xrange(M):
        type, start, end = li1[j]
        if type & 1:
            root = queryOne(root, start, end)
        else:
            root = queryTwo(root, start, end)
            
        getOutput(root)
            
    
        
    
            
        
        
