# URL : http://www.geeksforgeeks.org/find-the-k-most-frequent-words-from-a-file/

file = '''Welcome to the world of Geeks 
This portal has been created to provide well written well thought and well explained 
solutions for selected questions If you like Geeks for Geeks and would like to contribute 
here is your chance You can write article and mail your article to contribute at 
geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help 
thousands of other Geeks'''

#file = "Welcome to the world of Geeks Geeks"


class TrieNode:
    def __init__(self):
        self.frequency = 0
        self.indexMinHeap = -1
        self.isEnd = False
        self.childs = [None] * 26
        
class MinHeapNode:
    def __init__(self):
        self.node = None
        self.frequency = 0
        self.word = None
        
        
def swap(li, a, b):
    li[a], li[b] = li[b], li[a]
    
    
def insertInHeap(trieNode,word):
    if trieNode.indexMinHeap == -1:
        if len(heap) < K:
            print "Insert in heap"
            heapNode = MinHeapNode()
            heapNode.node = trieNode
            heapNode.frequency = trieNode.frequency
            heapNode.word = word
            
            heap.append(heapNode)
            trieNode.indexMinHeap = len(heap) - 1
            percolateup(heapNode, (len(heap) - 2) >> 1, len(heap))
        else:
            "Check the frequency with top adn if it is greater than that than delete and insert this element"
            if heap[0].frequency < trieNode.frequency:
                print "Delete and insert"
                heapNode = MinHeapNode()
                heapNode.node = trieNode
                heapNode.frequency = trieNode.frequency
                heapNode.word = word
                
                
                heap[0].node.indexMinHeap = -1
                heap[0].node = None
                heap[0] = heapNode
                trieNode.indexMinHeap = 0
                percolateDown(trieNode, 0, len(heap))
    else:
        print "Increase the frequency and percolate down"
        heap[trieNode.indexMinHeap].frequency += 1
        percolateDown(trieNode, trieNode.indexMinHeap, len(heap))
        
    


    
def percolateDown(node, index, length):
    child1 = 2 * index + 1
    child2 = (child1 + 1) if (child1 + 1) < length else 0
    minchild = child1
    if child2 != 0 and heap[child2].frequency < heap[child1].frequency:
        minchild = child2
    while minchild < length and heap[minchild].frequency < heap[index].frequency:
        # swap the pointers of trie as well
        heap[index].node.indexMinHeap, heap[minchild].node.indexMinHeap = minchild, index
        # swap end
        
        heap[index], heap[minchild] = heap[minchild], heap[index]
        
        
        index = minchild
        child1 = 2 * index + 1
        child2 = (child1 + 1) if (child1 + 1) < length else 0
        minchild = child1
        if child2 != 0 and heap[child2].frequency < heap[child1].frequency:
            minchild = child2
            
            
def percolateup(node, index, length):
    child1 = 2 * index + 1
    child2 = (child1 + 1) if (child1 + 1) < length else 0
    minchild = child1
    if child2 != 0 and heap[child2].frequency < heap[child1].frequency:
        minchild = child2
        
    while minchild >= 0 and heap[minchild].frequency > heap[index].frequency:
        # swap the pointers of trie as well
        heap[index].node.indexMinHeap, heap[minchild].node.indexMinHeap = minchild, index
        # swap end
        
        heap[index], heap[minchild] = heap[minchild], heap[index]
        index = (index - 1) >> 1
        child1 = 2 * index + 1
        child2 = (child1 + 1) if (child1 + 1) < length else 0
        minchild = child1
        if child2 != 0 and heap[child2].frequency < heap[child1].frequency:
            minchild = child2
        
    
def insertInTrieUtil(root, word, index):
    if root is None:
        root = TrieNode()
        
    if index == len(word):
        root.isEnd = True
        root.frequency += 1
        insertInHeap(root,word)
    else:
        ni = ord(word[index]) - 97
        root.childs[ni] = insertInTrieUtil(root.childs[ni], word, index + 1)
        
    
    return root
    

def insertInTrie(root, word):
    return insertInTrieUtil(root, word, 0)



root = None
heap = []
K = 5
for word in file.split():
    root = insertInTrie(root, word.lower())
    print "_________________________________"
    for element in heap:
        print element.word,element.frequency
    print "_________________________________"
    
