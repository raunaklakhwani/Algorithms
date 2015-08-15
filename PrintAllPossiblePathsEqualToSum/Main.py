from copy import deepcopy
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
    # d[3] = [None, 6]
    # d[4] = [7, 8]
    # d[6] = [10]
    # return d
    #===========================================================================
    
    d = {}
    d[1] = [2, 3]
    d[2] = [4, 5]
    return d

def merge(o, left, right, data, sum):
    reqsum = sum - data
    
    if len(left) and len(right):
        for i in left:
            for j in right:
                if i + j == reqsum and (len(left[i]) or len(right[j])):
                    if len(left[i]) and len(right[j]):
                        m = deepcopy(left[i])
                        m.append(data)
                        m.extend(right[j])
                        checkPath.paths.append(m)
                    elif len(left[i]):
                        m = deepcopy(left[i])
                        m.append(data)
                        checkPath.paths.append(m)
                    elif len(right[j]):
                        m = deepcopy(right[j])
                        m.append(data)
                        checkPath.paths.append(m)
                        
                        
    
    if len(left):
        for i in left:
            if i == sum:
                m = deepcopy(left[i])
                checkPath.paths.append(m)
                
    if len(right):
        for i in right:
            if i == sum:
                m = deepcopy(right[i])
                checkPath.paths.append(m)
                
    if len(left):
        for i in left:
            if len(left[i]):
                m = o.get(i + data, [])
                x = deepcopy(left[i])
                x.append(data)
                m.extend(x)
                o[i + data] = m
            
    if len(right):
        for i in right:
            if len(right[i]):
                m = o.get(i + data, [])
                x = deepcopy(right[i])
                x.append(data)
                m.extend(x)
                o[i + data] = m
                
    o.setdefault(0,[])
            
    print
    

def checkPathUtil(root, sum):
    if root is None:
        return {0:[]}
    elif root.left is None and root.right is None:
        return {0:[], root.data:[root.data]}
    else:
        l = {}
        data = root.data
        left = checkPathUtil(root.left, sum)
        right = checkPathUtil(root.right, sum)
        l[data] = [data]
        merge(l, left, right, data, sum)
        return l
        
        

def checkPath(root, sum):
    checkPath.paths = []
    checkPathUtil(root, sum)
    print checkPath.paths
    print 

if __name__ == '__main__':
    d = getTreeDict()
    root = constructTree(d, 1)
    checkPath(root, 4)
    
