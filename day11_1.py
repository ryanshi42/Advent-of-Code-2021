def executeCycle(rowList, numFlashes):
    newRowList, flashList, numFlashes = executeNormal(rowList, [], numFlashes)
    # change = True
    visited = []
    # while change is True:
    #     change = False
    #     oldFlashList = []
    #     newRowList, flashList, numFlashes = executeFlashes(rowList, flashList, visited, numFlashes)
    #     if oldFlashList != flashList:
    #         change = True
    #     visited.add(set(flashList))
    newRowList, numFlashes = executeFlashes(newRowList, flashList, [], numFlashes)
    return newRowList, numFlashes

def executeFlashes(rowList, flashList, visited, numFlashes):
    newRowList = rowList
    ultFlashList = flashList
    while len(flashList) > 0:
        octoFlash = flashList.pop(0)
        visited.append(octoFlash)
        # print(flashList)
        newFlashList = []
        i = octoFlash[0]
        j = octoFlash[1]
        # print(i, j)
        if i > 0:
            if j > 0:
                newRowList, newFlashList, visited = alterRows(i - 1, j - 1, newRowList, visited, ultFlashList, newFlashList)

            newRowList, newFlashList, visited = alterRows(i - 1, j, newRowList, visited, ultFlashList, newFlashList)

            if j + 1 < len(rowList[0]):
                newRowList, newFlashList, visited = alterRows(i - 1, j + 1, newRowList, visited, ultFlashList,newFlashList)

            
        if i + 1 < len(rowList):
            if j > 0:
                newRowList, newFlashList, visited = alterRows(i + 1, j - 1, newRowList, visited, ultFlashList, newFlashList)
            newRowList, newFlashList, visited = alterRows(i + 1, j, newRowList, visited, ultFlashList,newFlashList)
            if j + 1 < len(rowList[0]):
                newRowList, newFlashList, visited = alterRows(i + 1, j + 1, newRowList, visited, ultFlashList, newFlashList)
        
        if j > 0:
            newRowList, newFlashList, visited = alterRows(i, j - 1, newRowList, visited, ultFlashList, newFlashList)
        if j + 1 < len(rowList[0]):
            newRowList, newFlashList, visited = alterRows(i, j + 1, newRowList, visited, ultFlashList, newFlashList)
        
        numFlashes += len(newFlashList)
        # print(numFlashes)
        flashList += newFlashList
        flashList = list(set(flashList))
        ultFlashList += newFlashList
        # print(newRowList)

        # print(flashList)
        # print(visited + newFlashList + flashList)
    return newRowList, numFlashes

def alterRows(i, j, rowList, visited,flashList, newFlashList):
    rowEntry = rowList[i][j]
    if (i, j) in visited:
        return rowList, newFlashList, visited
    if (i, j) not in flashList:
        rowList[i][j] = (rowList[i][j] + 1) % 10
    if int(rowEntry) == 9:
        newFlashList.append((i, j))
        # if (i, j) not in visited:
        #     visited.append((i, j))
    return rowList, newFlashList, visited

    
def executeNormal(rowList, flashList, numFlashes):
    for i, row in enumerate(rowList):
        for j, rowEntry in enumerate(row):
            if int(rowEntry) == 9:
                flashList.append((i, j))
                numFlashes += 1
    newRowList = [[(int(rowEntry) + 1) % 10 for rowEntry in row] for row in rowList]
    return newRowList, flashList, numFlashes

argList = []
rowList = []

with open('day11_1.in') as f:
    argList = f.readlines()

rowList = [arg.split()[0] for arg in argList]
print(rowList)

numSteps = 100
numFlashes = 0

for step in range(numSteps):
    rowList, numFlashes = executeCycle(rowList, numFlashes)
print(rowList)
print()
print(numFlashes)

