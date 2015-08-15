# URL : https://www.hackerrank.com/challenges/swap-nodes-algo
from collections import deque
import sys
sys.setrecursionlimit(1500)
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def getTreeFromInorderPreorder():
    N = input()
    root = Node(1, None, None)
    q = deque([root])
    for _ in xrange(N):
        l, r = map(int, raw_input().split())
        item = q.popleft()
        if l != -1:
            item.left = Node(l, None, None)
            q.append(item.left)
        if r != -1:
            item.right = Node(r, None, None)
            q.append(item.right)
    return root
        

def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.data ,
        inorder(root.right)

def swap(root, level, K):
    if root is not None:
        if level % K == 0:
            root.left, root.right = root.right, root.left
        swap(root.left, level + 1, K)
        swap(root.right, level + 1, K)
         
        
if __name__ == '__main__':
    root = getTreeFromInorderPreorder()
    for _ in xrange(input()):
        swap(root, 1, input())
        inorder(root)
        print
        
