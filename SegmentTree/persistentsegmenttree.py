# https://www.hackerrank.com/contests/morgan-stanley-2015/challenges/wet-shark-and-kth-largest-number

from collections import defaultdict

class Node:
    def __init__(self, left, right, count):
        self.left = left
        self.right = right
        self.count = count
        
def insert(start, end, root, num):
    if num >= start and num <= end:
        if root is None:
            root = Node(None, None, 0)
        
        if start == end:
            return Node(root.left, root.right, root.count + 1)
        else:
            mid = (start + end) >> 1
            left = insert(start, mid, root.left, num)
            right = insert(mid + 1, end, root.right, num)
            lw = left.count if left else 0
            rw = right.count if right else 0
            return Node(left, right, lw + rw)
    else:
        return root
    
def query(start, end, a, kth):
    if start == end:
        return start
    z = a.left.count if a.left else 0
    mid = (start + end) >> 1
    if z >= kth:
        result = query(start, mid, a.left, kth)
    else:
        result = query(mid + 1, end, a.right, kth - z)
    return result

# maximum = 100001
maximum = float("-inf")
root = Node(None, None, 0)


if __name__ == '__main__':
    a, b = map(int, raw_input().split())
    li = map(int, raw_input().split())
    
    indices = defaultdict(list)
    for g in xrange(a):
        indices[li[g]].append(g)
        maximum = max(maximum, li[g])
    # print indices
    x = [None] * (maximum + 2)
    x[-1] = root
    
    for g in xrange(maximum, -1, -1):
        x[g] = x[g + 1]
        if indices.get(g):
            for y in xrange(len(indices[g])):
                x[g] = insert(0, len(li) - 1, x[g], indices[g][y])
    
    del indices
    
    for g in xrange(b):
        above, kth = map(int, raw_input().split())
        result = li[query(0, len(li) - 1, x[above], kth)]
        print result
        
    
