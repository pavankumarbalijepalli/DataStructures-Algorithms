from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, v)
        print(stack)
    
    def topologicalSort(self):
        visited = []
        stack = []

        for i in list(self.graph):
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        print(stack)
        # print(visited)

custGraph = Graph(8)
custGraph.addEdge("A", "C")
custGraph.addEdge("C", "E")
custGraph.addEdge("E", "H")
custGraph.addEdge("E", "F")
custGraph.addEdge("F", "G")
custGraph.addEdge("B", "C")
custGraph.addEdge("B", "D")
custGraph.addEdge("D", "F")
# print(custGraph.graph)
custGraph.topologicalSort()

