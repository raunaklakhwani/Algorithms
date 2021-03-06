from _collections import deque
class Node:
    def __init__(self,data,end,left,equal,right):
        self.data = data
        self.end = end
        self.left = left
        self.equal = equal
        self.right = right

def levelOrder(root):
    print "Level order = "
    print "_________________________"
    if root:
        q = deque([root,None])
        while len(q):
            item = q.popleft()
            if item:
                print (item.data,item.end),
                if item.left:
                    q.append(item.left)
                if item.equal:
                    q.append(item.equal)
                if item.right:
                    q.append(item.right)
            else:
                print
                if len(q) == 0:
                    break
                q.append(None)
            
    print "_________________________"
    

def createTernarySearchTree(inp):
    root = None
    if len(inp):
        for s in inp:
            root = addNode(root, s)
    return root

def addNode(root,s):
    if root is None:
        if len(s) == 1:
            root = Node(s[0],1,None,None,None)
            return root
        elif len(s) == 0:
            return root
        else:
            root = Node(s[0],0,None,None,None)
            root.equal = addNode(root.equal,s[1:])
            return root
    else:
        if len(s) == 0:
            root.end = 1
            return root
        else:
            if s[0] > root.data:
                root.right = addNode(root.right, s)
            elif s[0] < root.data:
                root.left = addNode(root.left,s)
            else:
                root.equal = addNode(root.equal, s[1:])
            
            return root

def search(root,s):
    found = False
    if root is not None:
        if len(s):
            if s[0] > root.data:
                found = search(root.right,s)
            elif s[0] < root.data:
                found = search(root.left,s)
            elif s[0] == root.data:
                if len(s) == 1:
                    if root.end == 1:
                        found = True
                    else:
                        found = False
                else:
                    found = search(root.equal,s[1:])
    
    return found
        
    
        
if __name__ == '__main__':
    inp = ["cat","bug","cats","up"]
    inp = map(str.upper,inp)
    root = createTernarySearchTree(inp)
    levelOrder(root)
    print search(root, "CA")
    print search(root, "CAT")
    print search(root, "")