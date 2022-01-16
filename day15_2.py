def neighbours(i, j, gridLen):
    nList = []
    if i > 0:
        nList.append((i - 1, j))
    if j + 1 < gridLen:
        nList.append((i, j + 1))
    if i + 1 < gridLen:
        nList.append((i + 1, j))
    if j > 0:
        nList.append((i, j - 1))
    return nList
    
def dupRow(l):
    toReturn = l
    for _ in range(4):
        l = [elem % 9 + 1 for elem in l]
        toReturn += l

    return toReturn

def dupRowRow(g):
    toReturn = g
    y = g
    for _ in range(4):
        newY = []
        for l in y:
            x = [elem % 9 + 1 for elem in l]
            newY.append(x)
        y = newY
        toReturn += y
        
    return toReturn

grid = open('day15_1.in').read().split('\n')


# sumGrid = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
grid = [[int(elem) for elem in grid[i]] for i, _ in enumerate(grid)]
grid = [(dupRow(row)) for row in grid]
grid = dupRowRow(grid)
# print(grid)
gridLen = len(grid)

# sumGrid[0][0] = 0
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if i == 0 and j == 0:
#             continue
#         if i == 0:
#             sumGrid[i][j] += int(sumGrid[i][j - 1])
#         elif j == 0:
#             sumGrid[i][j] += int(sumGrid[i - 1][j])
#         else: 
#             sumGrid[i][j] += min(int(sumGrid[i][j - 1]), int(sumGrid[i - 1][j]))

# print(sumGrid)
# print(sumGrid[len(grid[0]) - 1][len(grid) - 1])
        
distance = {}
prev = {}
pq = [(0, (0,0))]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        distance[(i, j)] = 9999
        prev[(i, j)] = None
distance[(0,0)] = 0
while len(pq) > 0:
    pq.sort(key=lambda x : x[0])
    u = pq.pop(0)
    
    # del distance[u]
    for v in neighbours(u[1][0], u[1][1], gridLen):
        if distance[v] > u[0] + grid[v[0]][v[1]]:
            distance[v] = u[0] + grid[v[0]][v[1]]
            pq.append((distance[v], v))

print(distance[(gridLen - 1, gridLen - 1)])