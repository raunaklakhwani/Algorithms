# URL : http://www.geeksforgeeks.org/custom-tree-problem/

class Node:
    def __init__(self, data, childs):
        self.data = data
        self.childs = childs


def searchNode(root, data):
    if root is not None:
        if root.data == data:
            return root
        for child in root.childs:
            found = searchNode(child, data)
            if found:
                return found
        
    return None
        

def getTrees(inp):
    trees = []
    for s in inp:
        l, r = s.split()
        rightNode = leftNode = None
        leftFound = False
        rightFound = False
        for tree in trees:
            ln = searchNode(tree, l)
            if ln:
                leftFound = True
                leftNode = ln
            
            if r == tree.data:
                rightNode = tree
                rightFound = True
            
            if leftFound and rightFound:
                leftNode.childs.append(rightNode)
                trees.remove(rightNode)
                break
            
        if leftFound and rightFound == False:
            leftNode.childs.append(Node(r,[]))
            
                
        if leftFound == False and rightFound == False:
            leftNode = Node(l, [Node(r, [])])
            trees.append(leftNode)
    return trees

def printTree(root, prefix):
    if root is not None:
        print prefix, "-->", root.data
        for child in root.childs:
            printTree(child, "   |" + prefix)

def printTrees(trees):
    for root in trees:
        printTree(root, "")
        print
        
        

def printIndentedTree(inp):
    trees = getTrees(inp)
    printTrees(trees)

if __name__ == '__main__':
    #inp = ["z y", "a b", "z a", "a g", "b c", "c d", "d e", "c f", "y x", "x w"]
    inp = ["z y", "a b", "a g", "b c", "c d", "d e", "c f", "y x", "x w"]
    printIndentedTree(inp)
    
