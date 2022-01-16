def checkLowPoints(i, j, rowList):
    currHeight = int(rowList[i][j])
    if i != 0 and int(rowList[i - 1][j]) <= currHeight:
        return False
    if i + 1 != len(rowList) and int(rowList[i + 1][j]) <= currHeight:
        return False
    if j != 0 and int(rowList[i][j - 1]) <= currHeight:
        return False
    if j + 1 != len(rowList[i]) and int(rowList[i][j + 1]) <= currHeight:
        return False

    return True

def calculateSize(lowPoint, basinSizeList, basinPointList, rowList):
    basinSize = 0
    currPoint = lowPoint
    queue = [currPoint]
    while len(queue) != 0:
        currPoint = queue.pop(0)
        basinPointList.append(currPoint)
        i = currPoint[0]
        j = currPoint[1]
        if i != 0 and int(rowList[i - 1][j]) != 9 and (i-1, j) not in basinPointList and (i-1, j) not in queue:
            queue.append((i-1, j))
        if i + 1 != len(rowList) and int(rowList[i + 1][j]) != 9 and (i+1, j) not in basinPointList and (i+1, j) not in queue:
            queue.append((i + 1, j))
        if j != 0 and int(rowList[i][j - 1]) != 9 and (i, j - 1) not in basinPointList and (i, j - 1) not in queue:
            queue.append((i, j - 1))
        if j + 1 != len(rowList[i]) and int(rowList[i][j + 1]) != 9 and (i, j+1) not in basinPointList and (i, j + 1) not in queue:
            queue.append((i, j + 1))
        basinSize += 1
        # print(currPoint)
    basinSizeList.append(basinSize)
    return basinSizeList, basinPointList

rowList = []

with open('day9_1.in') as f:
    rowList = [row.strip() for row in f.readlines()]
    # rowList = [row.strip() for row in '''2199943210
    # 3987894921
    # 9856789892
    # 8767896789
    # 9899965678'''.split("\n")]
    print(rowList)

i = 0
j = 0
count = 0
lowPointList = []
basinPointList = []
basinSizeList = []

while i < len(rowList):
    j = 0
    while j < len(rowList[i]):
        if checkLowPoints(i, j, rowList) is True:
            riskLevel = 1 + int(rowList[i][j])
            lowPointList.append((i, j))
            count += riskLevel
        j += 1
    i += 1

for lowPoint in lowPointList:
    if lowPoint in basinPointList:
        continue
    basinSizeList, basinPointList = calculateSize(lowPoint, basinSizeList, basinPointList, rowList)
    # calculate the size of each basin they are in
    # if a basin contains any lowPoint, skip over it

print(basinSizeList)

multiplier = 1
for _ in range(3):
    temp = max(basinSizeList)
    multiplier *= temp
    basinSizeList.remove(temp)
print(multiplier)

# correct answer, uses a 3d array, product function

# from math import prod

# def recursive_fill_basins(x, y, array):
#     if array[x][y][0] == 9 or array[x][y][1]:
#         return 0
#     array[x][y] = (array[x][y][0], True)
#     total = 1
#     total += recursive_fill_basins(x - 1, y, array) if x - 1 >= 0 else 0
#     total += recursive_fill_basins(x + 1, y, array) if x + 1 < len(array) else 0
#     total += recursive_fill_basins(x, y - 1, array) if y - 1 >= 0 else 0
#     total += recursive_fill_basins(x, y + 1, array) if y + 1 < len(array[0]) else 0
#     return total

# if __name__ == '__main__':
#     array = [[(int(value), False) for value in line[:-1]] for line in open('input.in')]
#     totals = [recursive_fill_basins(x, y, array) for x in range(len(array)) for y in range(len(array[0]))]

#     print(prod(sorted(totals)[-3:]))