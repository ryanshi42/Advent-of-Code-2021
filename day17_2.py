import math

# returns the maximum number of steps
def calculateXDragSteps(xBottom, xTop):
    n = math.floor(math.sqrt(xBottom * 2))
    while (n * (n+1)) / 2 <= xTop:
        n += 1
    return n - 1

def eradicate(xBottom, xTop, yBottom, yTop):
    satisfyingSet = set()
    # 78, 22
    maxY = 78
    for i in range(yBottom, maxY + 1):
        for j in range(0, xTop + 1):
            satisfyingSet.add((j, i))
    newSet = set()
    for t in satisfyingSet:
        if eventuallyHit(t, xBottom, xTop, yBottom, yTop):
            newSet.add(t)
    print(newSet)
    return newSet

def eventuallyHit(t, xBottom, xTop, yBottom, yTop):
    xCoord = 0
    yCoord = 0
    xVelocity = t[0]
    yVelocity = t[1]
    while xCoord <= xTop and yCoord >= yBottom:
        xCoord += xVelocity
        yCoord += yVelocity
        if xCoord in range(xBottom, xTop + 1) and yCoord in range(yBottom, yTop + 1):
            return True 
        xVelocity -= 1 if xVelocity != 0 else 0
        yVelocity -= 1
    return False



argList = open('day17_1.in').read()[13:].split(', ')
# print(argList)

for coord in argList:
    if coord.split('..')[0][0] == 'x':
        xBottom = int(coord.split('..')[0][2:])
        xTop = int(coord.split('..')[1])
    else:
        yBottom = int(coord.split('..')[0][2:])
        yTop = int(coord.split('..')[1])

print(xBottom, xTop, yBottom, yTop)
maxSteps = calculateXDragSteps(xBottom, xTop)
print(maxSteps)
# maxVelocity = calculateYDragSteps(maxSteps, yBottom, yTop)
maxVelocity = 77
print(maxVelocity)
# max y velocity is 77
# max x velocity is 22
print(len(eradicate(xBottom, xTop, yBottom, yTop)))
print((maxVelocity * (maxVelocity + 1)) / 2)

# print(eventuallyHit((7, -1), xBottom, xTop, yBottom, yTop))

# get there in one step:
# get there in two steps:

