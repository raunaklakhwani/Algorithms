#URL : http://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        

def getTreeUtil(start, end):
    li = []
    if start > end:
        return [None]
    for i in xrange(start, end + 1):
        left = getTreeUtil(start, i - 1)
        right = getTreeUtil(i + 1, end)
        
        for l in left:
            for r in right:
                root = Node(i, None, None)
                root.left = l
                root.right = r
                li.append(root)
    return li
                
    
    
        
if __name__ == '__main__':
    N = 5
    li = getTreeUtil(0, 4)
    print len(li)
    
    
    
    
