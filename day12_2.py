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
        # print(visited)
        caveVisitList = []
        for node in visited:
            if node[0] == current:
                caveVisitList.append(node[1])
        if caveVisitList != []:
            visited.add((current, max(caveVisitList) + 1))
        else:
            visited.add((current, 1))

        canDup = True
        for node in visited:
            if node[0] != 'start' and node[0].islower() and node[1] == 2:
                canDup = False

        if current == 'end':
            print(path)
            self.numPaths += 1
        else: 
            for cave in self.graph[current]:
                if cave.islower() and (cave, 1) in visited and not canDup:
                    pass
                elif cave == 'start':
                    pass
                else:
                    self.dfs(cave, visited, path)

        path.pop()
        caveVisitList = []
        for node in visited:
            if node[0] == current:
                caveVisitList.append(node[1])
        visited.remove((current, max(caveVisitList)))

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

# print(graph)
print(g.numPaths)
