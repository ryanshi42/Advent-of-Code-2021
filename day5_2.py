argList = []
pointsDict = {}


for line in open("day5_1input.txt"):
    line = line.strip()
    argList.append(line)

for arg in argList:
    euclideanLine = arg.split(" -> ")
    point0 = tuple(euclideanLine[0].split(','))
    point1 = tuple(euclideanLine[1].split(','))
    if int(point0[0]) == int(point1[0]):
        if (int(point0[1]) < int(point1[1])):
            for i in range(int(point0[1]), int(point1[1]) + 1):
                pointsDict[(int(point0[0]), i)] = pointsDict.get((int(point0[0]), i), 0) + 1
        else:
            for i in range(int(point1[1]), int(point0[1]) + 1):
                pointsDict[(int(point0[0]), i)] = pointsDict.get((int(point0[0]), i), 0) + 1
    elif int(point0[1]) == int(point1[1]):
        if (int(point0[0]) < int(point1[0])):
            for i in range(int(point0[0]), int(point1[0]) + 1):
                pointsDict[(i, int(point0[1]))] = pointsDict.get((i, int(point0[1])), 0) + 1
        else:
            for i in range(int(point1[0]), int(point0[0]) + 1):
                pointsDict[(i, int(point0[1]))] = pointsDict.get((i, int(point0[1])), 0) + 1
    elif int(point0[0]) < int(point1[0]):
        if (int(point0[1]) < int(point1[1])):
            for i in range(int(point1[1]) - int(point0[1]) + 1):
                pointsDict[(int(point0[0]) + i, int(point0[1]) + i)] = pointsDict.get((int(point0[0]) + i, int(point0[1]) + i), 0) + 1
        else:
            for i in range(int(point0[1]) - int(point1[1]) + 1):
                pointsDict[(int(point0[0]) + i, int(point0[1]) - i)] = pointsDict.get((int(point0[0]) + i, int(point0[1]) - i), 0) + 1
    else:
        if (int(point0[1]) < int(point1[1])):
            for i in range(int(point1[1]) - int(point0[1]) + 1):
                pointsDict[(int(point0[0]) - i, int(point0[1]) + i)] = pointsDict.get((int(point0[0]) - i, int(point0[1]) + i), 0) + 1
        else:
            for i in range(int(point0[1]) - int(point1[1]) + 1):
                pointsDict[(int(point0[0]) - i, int(point0[1]) - i)] = pointsDict.get((int(point0[0]) - i, int(point0[1]) - i), 0) + 1
        
print(argList)
print(pointsDict)
print(len([k for k, v in pointsDict.items() if v >= 2]))
        