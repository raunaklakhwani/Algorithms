# URL : http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
from heapq import heappop, heappush
inp = [1, 23, 12, 9, 30, 2, 50]
k = 3



def getLargestKElement(inp, k):
    heap = []
    for i in xrange(len(inp)):
        if i < k:
            heappush(heap, inp[i])
        else:
            if inp[i] > heap[0]:
                heappop(heap)
                heappush(heap, inp[i])
                
    return heap
        
    

if __name__ == '__main__':
    print getLargestKElement(inp, k)
