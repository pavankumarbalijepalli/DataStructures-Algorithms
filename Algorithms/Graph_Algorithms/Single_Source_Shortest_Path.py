class Graph:
    def __init__(self, gdict):
        if not gdict:
            gdict = {}
        self.gdict = gdict

    def sssp(self, start, end):
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            print(path)
            node = path[-1]
            if node == end:
                return path
            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

gdict = {'A': ['B', 'C'],
         'B': ['D'],
         'C': ['E'],
         'D': ['C'],
         'E': ['B']}

custGraph = Graph(gdict)
custGraph.sssp('A', 'E')