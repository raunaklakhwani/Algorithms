#URL : http://www.geeksforgeeks.org/find-all-possible-interpretations/
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right



def inOrderUtil(root):
    if root is not None:
        inOrderUtil(root.left)
        print root.data,
        inOrderUtil(root.right)
        
def inOrder(root):
    print "InOrder = ",
    inOrderUtil(root)
    print 

def getTreeUtil(inp, start, end):
    if start > end:
        return None
    elif start == end:
        return Node(inp[start], None, None)
    else:
        mid = start + (end - start) / 2
        root = Node(inp[mid], None, None)
        temp = root
        for i in xrange(mid - 1, -1, -1):
            temp.left = Node(inp[i], None, None)
            temp = temp.left
        temp = root
        for i in xrange(mid + 1, end + 1):
            temp.right = Node(inp[i], None, None)
            temp = temp.right
            
        #root = Node(2,Node(1,Node(1,None,None),None),None)
            
        
        
        # root.left = getTreeUtil(start, mid - 1)
        # root.right = getTreeUtil(mid + 1, end)
        return root

def mergeLists(a, b):
    l = []
    if len(a) and len(b):
        for i in a:
            for j in b:
                l.append(i + j)
    elif len(a):
        l = a
    else:
        l = b
    return l
                

def getPermutationsUtil(root):
    if root is None:
        return []
    elif root.left is None and root.right is None:
        return [getPermutations.alphabets[root.data]]
    else:
        ans = []
        left = getPermutationsUtil(root.left)
        right = getPermutationsUtil(root.right)
        dataList = [getPermutations.alphabets[root.data]]
        ans.extend(mergeLists(mergeLists(left, dataList), right))
        
        if root.left:
            tempLeftData = root.left.data
            newData = int(str(root.left.data) + str(root.data))
            if newData <= 26:
                root.left.data = newData
                lp = getPermutationsUtil(root.left)
                ans.extend(mergeLists(lp, right))
                root.left.data = tempLeftData
        
        if root.right:
            tempRightData = root.right.data
            newData = int(str(root.data) + str(root.right.data))
            if newData <= 26:
                root.right.data = newData
                rp = getPermutationsUtil(root.right)
                ans.extend(mergeLists(left, rp))
                root.right.data = tempRightData
                
        return ans
            
                
        
        
        

def getPermutations(inp):
    getPermutations.alphabets = list("0abcdefghijklmnopqrstuvwxyz")
    root = getTreeUtil(inp, 0, len(inp) - 1)
    inOrder(root)
    l = getPermutationsUtil(root)
    return l
    
    
if __name__ == '__main__':
    inp = [1,1,2,1,2,1,1]
    l = getPermutations(inp)
    print l
    print len(l)
    
    
    
