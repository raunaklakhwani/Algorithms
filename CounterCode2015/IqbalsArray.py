class Node:
    def __init__(self, s1, s2, t1, t2, res, lazy, start, end, left, right, lazystart, lazyend,lazyType,lazyData):
        self.s1 = s1
        self.s2 = s2
        self.t1 = t1
        self.t2 = t2
        self.res = res
        self.lazy = lazy
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        self.lazystart = lazystart
        self.lazyend = lazyend
        self.lazyType = lazyType
        self.lazyData = lazyData
        

def queryOne(root,s,e,add):
    if root.start <= s and root.end >= e:
        if root.lazy:
            if root.lazyType == 1:
                root.s1 += root.lazyData
                root.t1 += (root.end - root.start + 1) * root.lazyData
                root.res += (root.lazyData * root.t2)
                root.lazy = False
                if root.left:
                    root.left.lazy = True
                    root.left.lazyType = root.lazyType
                    root.left.lazyData = root.lazyData
                if root.right:
                    root.right.lazy = True
                    root.right.lazyType = root.lazyType
                    root.right.lazyData = root.lazyData
                    
        
                
        print "Covered"
        
        
N, Q = 5, 3
root = Node(0, 0, 0, 0, 0, False, 1, N, None, None, 0, 0)

for _ in xrange(Q):
    query = map(int,raw_input().split())
    if query[0] == 1:
        s = query[1]
        e = query[2]
        add = query[3]

