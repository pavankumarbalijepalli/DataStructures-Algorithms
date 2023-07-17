from inspect import stack
from re import L


class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if (vertex1 and vertex2) not in self.adjacency_list:
            return False
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return True

    def remove_edge(self, vertex1, vertex2):
        if (vertex1 and vertex2) not in self.adjacency_list:
            return False
        self.adjacency_list[vertex1] = list(set(self.adjacency_list[vertex1]) - set([vertex2]))
        self.adjacency_list[vertex2] = list(set(self.adjacency_list[vertex2]) - set([vertex1]))
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            return False
        for i in self.adjacency_list[vertex]:
            self.remove_edge(i, vertex)
        del self.adjacency_list[vertex]
        return True

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, ":", edges) 
        print('-'*15)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue: 
            deVertex = queue.pop(0)
            print(deVertex)
            for adj in self.adjacency_list[deVertex]:
                if adj not in visited:
                    visited.append(adj)
                    queue.append(adj)
    
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            deStack = stack.pop()
            print(deStack)
            for adj in self.adjacency_list[deStack]:
                if adj not in visited:
                    visited.append(adj)
                    stack.append(adj)
    

if __name__ == "__main__":
    customGraph = Graph()
    customGraph.add_vertex('A')
    customGraph.add_vertex('B')
    customGraph.add_vertex('C')
    customGraph.add_vertex('D')
    customGraph.add_edge(vertex1='A',vertex2='B')
    customGraph.add_edge(vertex1='A',vertex2='C')
    customGraph.add_edge(vertex1='B',vertex2='C')
    customGraph.add_edge(vertex1='B',vertex2='D')
    customGraph.add_edge(vertex1='C',vertex2='D')
    # customGraph.print_graph()
    # customGraph.remove_vertex(vertex='D')
    customGraph.print_graph()
    customGraph.bfs('A')
    print('-'*5)
    customGraph.dfs('A')
    # customGraph.remove_edge(vertex1='A', vertex2='B')
    # customGraph.print_graph()