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

rowList = 0

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

while i < len(rowList):
    j = 0
    while j < len(rowList[i]):
        if checkLowPoints(i, j, rowList) is True:
            riskLevel = 1 + int(rowList[i][j])
            print((i, j))
            count += riskLevel
        j += 1
    i += 1

print(count)

# def somethingLower(x: int, y: int, value: int, array: list[list[int]]):
#     return (x - 1 >= 0 and array[x - 1][y] <= value) or (x + 1 < len(array) and array[x + 1][y] <= value) \
#     or (y - 1 >= 0 and array[x][y - 1] <= value) or (y + 1 < len(array[0]) and array[x][y + 1] < value)

# if __name__ == '__main__':
#     array = [[int(value) for value in line[:-1]] for line in open('example.in')]
#     answer = 0
#     for x, row in enumerate(array):
#         for y, value in enumerate(row):
#             if not somethingLower(x, y, value, array):
#                 answer = answer + 1 + value
#     print(answer)