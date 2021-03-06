from pprint import pprint
import heapq
import Queue
import copy
from unionfind import unionfind
class UndirectedGraph:
    def __init__(self, edges):
        self.adjacencyList = {}
        for edge in edges:
            source,destination,cost = edge
            self.adjacencyList.setdefault(source,[]).append((destination,cost))
            self.adjacencyList.setdefault(destination,[]).append((source,cost))

    def prims(self):
        vertices = self.adjacencyList.keys()
        source = vertices[0]
        heap = [(0,(source,source,0))]
        heapq.heapify(heap)
        minS = []
        seen = set()
        while len(minS) != len(vertices):
            pop = heapq.heappop(heap)
            minS.append(pop[1])
            s = pop[1][1]
            seen.add(s)
            connections = self.adjacencyList[s]
            for (d,cost) in connections:
                if d not in seen:
                    heapq.heappush(heap, (cost,(s,d,cost)))
        del minS[0]
        return minS
    
    def kruskals(self):
        minS = []
        vertices = self.adjacencyList.keys()
        uf = unionfind(len(vertices))
        edges = []
        for vertex in vertices:
            for (d,c) in self.adjacencyList[vertex]:
                edges.append((vertex,d,c))
        
        edges = sorted(edges,key = lambda item: item[2])
        
        for (s,d,c) in edges:
            sIndex = vertices.index(s)
            dIndex = vertices.index(d)
            if uf.find(sIndex) != uf.find(dIndex):
                uf.unite(sIndex, dIndex)
                minS.append((s,d,c))
                
        return minS
                
            
        
        
                     
            
        
    
    
        
    def bfs(self,source):
        q = Queue.Queue()
        q.put(source)
        seen = set()
        while q.empty() != True:
            item = q.get()
            seen.add(item)
            for connect in self.adjacencyList[item]:
                if connect[0] not in seen:
                    q.put(connect[0])
        return seen
        
    def getConnectedComponents(self):
        vertices = self.adjacencyList.keys()
        connectedComponents = []
        seenComponents = set()
        for vertex in vertices:
            if vertex not in seenComponents:
                connectedComponent = self.bfs(vertex)
                seenComponents = seenComponents.union(connectedComponent)
                connectedComponents.append(connectedComponent)
        
        return connectedComponents
            
        
        
if __name__ == '__main__':
    graph = UndirectedGraph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
               ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
               ("e", "f", 9)])
    pprint(graph.adjacencyList)
    print "prims = ", graph.prims()
    print "Kruskals = ", graph.kruskals()
    print graph.bfs("a")
    print graph.getConnectedComponents()
    
    print "________________________"
    disconnectedGraph = UndirectedGraph([("a","b",1),("b","c",1),("c","a",1),("d","e",1),("f","g",1)])
    print disconnectedGraph.getConnectedComponents()