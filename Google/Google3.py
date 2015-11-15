class Node:
    def __init__(self, childs, data):
        self.data = data
        self.childs = childs
        
def getRootNode(rootData,d):
    if d.get(rootData):
        root = Node([],rootData)
        for child in d.get(rootData):
            childNode = getRootNode(child, d)
            if childNode:
                root.childs.append(childNode)
        return root
    return Node([],rootData)
    
def postorder(root):
    if root:
        for child in root.childs:
            postorder(child)
        print root.data, 
        
def postorderIterative(root):
    temp = root
    stack = []
    index = -1
    while True:
        while temp:
            stack.append((temp,0))
            if len(temp.childs):
                temp = temp.childs[0]
            else:
                temp = None
        
        if len(stack) == 0:
            break
        
        item,index = stack.pop()
        print item.data,
        
        parent,pi = stack[-1]
        while len(parent.childs) <= index + 1:
            if len(stack) == 0:
                break
            item,index = stack.pop()
            print item.data,
            if len(stack) == 0:
                break
            parent,pi = stack[-1]
            
        if len(stack) == 0:
            break
        temp = parent.childs[index + 1]
        stack.append((temp,index + 1))
        if len(temp.childs):
            temp = temp.childs[0]
        else:
            temp = None
            
            
            
        
        
        
        
            
        

if __name__ == '__main__':
    d = {1:[4, 8, 7], 4:[3, 9], 8:[18, 17], 7:[10], 3:[11], 10:[5]}
    root = getRootNode(1,d)
    postorder(root)
    print 
    postorderIterative(root)
    
