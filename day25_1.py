grid = open('day25_1.in').read().strip().split('\n')
newGrid = []

moved = True
steps = 0
while moved:
    newGrid = []
    moved = False
    steps += 1
    for i, row in enumerate(grid):
        newRow = []
        for j, elem in enumerate(row):
            if j != len(newRow):
                continue
            if elem == '>':
                # wraps around
                yCoord = j + 1 if j + 1 != len(grid[0]) else 0

                # if next elem is movable
                if (grid[i][yCoord] == '.'):
                    if yCoord == 0:
                        newRow[yCoord] = '>'
                        newRow.append('.')
                    else:
                        newRow.append('.')
                        newRow.append('>')
                    moved = True
                else:
                    newRow.append('>')
            else:
                newRow.append(elem)
        newGrid.append(newRow)
    # for x in range(len(newGrid)):
    #     r = ''
    #     for y in range(len(newGrid[x])):
    #         r += newGrid[x][y]
    #     print(r)
    # print()
    grid = [[e for e in row] for row in newGrid]

    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == 'v':

                # wraps around
                xCoord = i + 1 if i + 1 != len(grid) else 0

                # if next elem is movable
                if (grid[xCoord][j] == '.'):
                    newGrid[xCoord][j] = 'v'
                    moved = True
                    newGrid[i][j] = '.'

    # print(newGrid)
    # for x in range(len(newGrid)):
    #     r = ''
    #     for y in range(len(newGrid[x])):
    #         r += newGrid[x][y]
    #     print(r)
    print(moved, steps)
    grid = [[e for e in row] for row in newGrid]
    





