import heapq

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.min_distance = float('inf')
    
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight=weight, start_vertex=self, target_vertex=destination_vertex)
        self.neighbours.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        # Setting the minimum distance to 0 for starting vertex
        # because the distance two same vertices is 0
        start_vertex.min_distance = 0
        
        # Then we push the start_vertex into the heap
        heapq.heappush(self.heap, start_vertex)

        # Till the heap is empty
        while self.heap:

            # We take the minimum distance vertex and store it in a variable
            actual_vertex = heapq.heappop(self.heap)
            
            # If the vertex is visited we will skip the operation
            if actual_vertex.visited:
                continue

            # Going 
            for edge in actual_vertex.neighbours:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f'Shortest path to vertex is {vertex.min_distance} units')
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=' ')
            actual_vertex = actual_vertex.predecessor


nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(16, nodeE)

nodeC.add_edge(6, nodeD)
nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeB)





