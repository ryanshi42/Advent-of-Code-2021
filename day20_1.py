decoder, g = open('day20_1.in').read().split('\n\n')

grid = g.strip().split('\n')

def isValid(i, j):
    if i in range(len(grid)) and j in range(len(grid[0])):
        return True
    return False

def calculatePixel(i, j, parity):
    x = '.' if parity % 2 == 0 else decoder[0]
    ps = ''
    ps += grid[i-1][j-1] if i > 0 and j > 0 and isValid(i - 1, j - 1) else x
    ps += grid[i-1][j] if i > 0 and isValid(i - 1, j) else x
    ps += grid[i-1][j+1] if i > 0 and j + 1 < len(grid[0]) and isValid(i - 1, j + 1) else x
    ps += grid[i][j-1] if j > 0 and isValid(i, j - 1) else x
    ps += grid[i][j] if isValid(i, j) else x
    ps += grid[i][j+1] if j + 1 < len(grid[0]) and isValid(i, j + 1) else x
    ps += grid[i+1][j-1] if i + 1 < len(grid) and j > 0 and isValid(i + 1, j - 1) else x
    ps += grid[i+1][j] if i + 1 < len(grid) and isValid(i + 1, j) else x
    ps += grid[i+1][j+1] if i + 1 < len(grid) and j + 1 < len(grid[0]) and isValid(i + 1, j + 1) else x
    # try:
    #     ps += grid[i-1][j-1] 
    # except:
    #     ps += x
    # try:
    #     ps += grid[i-1][j]
    # except:
    #     ps += x
    # try:
    #     ps += grid[i-1][j+1]
    # except:
    #     ps += x
    # try:
    #     ps += grid[i][j-1] 
    # except:
    #     ps += x
    # try:
    #     ps += grid[i][j] 
    # except: 
    #     ps += x
    # try:
    #     ps += grid[i][j+1] 
    # except:
    #     ps += x
    # try:
    #     ps += grid[i+1][j-1]
    # except:
    #     ps += x
    # try:
    #     ps += grid[i+1][j]
    # except:
    #     ps += x
    # try:
    #     ps += grid[i+1][j+1]
    # except:
    #     ps += x
    ps = ps.replace('.','0').replace('#','1')
    return decoder[int(ps, 2)]


for k in range(50):
    print(k)
    newGrid = []
    for i in range(-1, len(grid) + 1):
        newRow = []
        for j in range(-1, len(grid[0]) + 1):
            newRow.append(calculatePixel(i, j, k))
        newGrid.append(newRow)
    grid = newGrid
    
    # for row in newGrid:
    #     [print(elem, end='') for elem in row]
    #     print()
    # grid = newGrid
    # print()


print(sum([row.count('#') for row in newGrid]))