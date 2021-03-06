
from pprint import pprint
import heapq
class Graph:
    def __init__(self, edges):
        self.adjacencyList = {}
        for edge in edges:
            source,destination,cost = edge
            self.adjacencyList.setdefault(source,[]).append((destination,cost))
            
    def dijkstra(self,source,target):
        '''
        Create a heap with items(cost,vertex,path)
        First add source to it.
        Then In the loop till heap is not empty
            pop the item.
            check that whether the popped item is already seen
            if not then add it to seen vertices and push its neighbours with updated cost to heap but also check while adding to heap that the neighbours are not already seen 
            
        Time Complexity is O(m log n) or O(m log m)
        '''
        
        heap = [(0,source,())]
        visited = set()
        while heap:
            cost,s,path = heapq.heappop(heap)
            if s not in visited:
                visited.add(s)
                path = (s,path)
                if s == target:
                    return (cost,path) 
                for d,c in self.adjacencyList.get(s,[]):
                    if d not in visited:
                        heapq.heappush(heap,(cost + c,d,path))
        return float('inf')
    
    
        
        


if __name__ == '__main__':
    graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
    pprint(graph.adjacencyList)
    
    # test caese for dijkstra starts
    #===========================================================================
    # pprint(graph.dijkstra("a", "e"))
    # vertices = graph.adjacencyList.keys()
    # for sourceVertex in vertices:
    #     for destinationVertex in vertices:
    #         #pprint(sourceVertex + " -- >" + destinationVertex)
    #         pprint(sourceVertex + " -- >" + destinationVertex + " == " +  str(graph.dijkstra(sourceVertex, destinationVertex)))
    #===========================================================================
    # test caese for dijkstra ends
    
    
    