import heapq

SOURCE_NODE=0
TARGET_NODE=1
EDGE_WEIGHT=2

DISTANCE_ROOT=3

def lesser(a:int,b:int):
    return a if a <= b else b


class Edge: 
    def __init__(self, time:list[int]):        
        self.target = time[TARGET_NODE]
        self.time = time[EDGE_WEIGHT]

    def __str__(self):
        return f' target: {self.target}, time: {self.time}'

class Vertex:
    def __init__(self, dist):
        self.srcRootDist = dist
        self.edges:list[Edge] = []
        self.visited = False

    def __str__(self):
        s=f' rootDist: {self.srcRootDist}, visited: {self.visited}, Edges: \n'
        for edge in self.edges:
            s+=f'\t{str(edge)}'
        
        return s

    def __lt__(self, other):
        return self.srcRootDist < other.srcRootDist
    

class Graph:
    
    def __init__(self, unvisited: list[list[int]], n):
        self.vertices:dict[int, Vertex] = {}
        for i in range(1, n + 1):
            self.vertices[i] = Vertex(float('inf'))
        for e in unvisited:              
            self.vertices[e[SOURCE_NODE]].edges.append(Edge(e))


    def getVertex(self, v)->Vertex:
        return self.vertices[v]

    def __str__(self):
        s=f'visits: {self.visitedVertices}\n'
        for key in self.vertices:
            s+=f'{key}: {str(self.vertices[key])}\n'

        return s


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph:Graph = Graph(times,n)

        graph.getVertex(k).srcRootDist = 0
        #print(graph)
        vertexHeap:list[Vertex] = []
        for i in range(1,n + 1):
            vertexHeap.append(graph.getVertex(i))

        #self.__printVertexHeap(vertexHeap)
        heapq.heapify(vertexHeap)
        #self.__printVertexHeap(vertexHeap)
        #print(graph)
        #while len(unvisited) > 0:
        #    print(heapq.heappop(unvisited))

        self.djikstra(graph, vertexHeap, n, k)
        #print(graph)


        maxDist = graph.getVertex(k).srcRootDist

        for i in range(1, n + 1):
            dist = graph.getVertex(i).srcRootDist
            if dist == float('inf'): return -1
            maxDist = max(dist, maxDist)

        return maxDist

    def __printVertexHeap(self,vertexHeap):
        for vertex in vertexHeap:
            print(vertex)

    def djikstra(self,graph:Graph, vertexHeap:list[Vertex], n, k):

        while len(vertexHeap) > 0:
            # pop unvisited vertex with smallest distance to starting node k
            vertex = heapq.heappop(vertexHeap)
            

            # visit the unvisited vertex
            self.djikstra_visit(graph, vertex)

            # heapify vertexHeap so min heap is updated after graph changes
            heapq.heapify(vertexHeap)

            #set vertex to visited
            vertex.visited = True

    def djikstra_visit(self, graph:Graph, vertex:Vertex):
        edges = vertex.edges
        vertexRdist = vertex.srcRootDist

        for edge in edges:
            target = graph.getVertex(edge.target)
            if not target.visited:
                pathDist = vertexRdist + edge.time
                target.srcRootDist = lesser(target.srcRootDist, pathDist)
                    

sol = Solution()

times=[[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
n=4
k=1

res = sol.networkDelayTime(times,n,k)

print(res)