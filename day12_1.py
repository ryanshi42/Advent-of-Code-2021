argList = []
graph = {}

class Graph:
    numPaths = 0
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, current, visited, path):
        path.append(current)
        if visited is None:
            visited = set()
        visited.add(current)

        if current == 'end':
            print(path)
            self.numPaths += 1
        else: 
            for cave in self.graph[current]:
                if cave.islower() and cave in visited:
                    pass
                else:
                    self.dfs(cave, visited, path)

        path.pop()
        visited.discard(current)

with open('day12_1.in') as f:
    argList = f.readlines()

for arg in argList:
    start = arg.split('-')[0].strip()
    end = arg.split('-')[1].strip()
    if graph.get(start, []) == []:
        graph[start] = [end]
    else:
        graph[start].append(end)    

    if graph.get(end, []) == []:
        graph[end] = [start]
    else:
        graph[end].append(start)
    g = Graph(graph)
    
g.dfs('start', set(), [])

print(graph)
print(g.numPaths)
