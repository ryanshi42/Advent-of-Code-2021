import math

# returns the maximum number of steps
def calculateXDragSteps(xBottom, xTop):
    n = math.floor(math.sqrt(xBottom * 2))
    while (n * (n+1)) / 2 <= xTop:
        n += 1
    return n - 1

def calculateYDragSteps(maxSteps, yBottom, yTop):
    satisfyingSet = set()
    if yTop >= 0:
        return ['help']
    counter = 0
    while counter < 3:
        for n in range(abs(yBottom)):
            magicNum = 0
            while True:
                if magicNum * n + (magicNum * (magicNum + 1)) / 2 in range(abs(yTop), abs(yBottom) + 1):
                    satisfyingSet.add(n)
                elif magicNum * n + (magicNum * (magicNum + 1)) / 2 > abs(yBottom):
                    break
                magicNum += 1

        maxSteps -= 1
        counter += 1
    return max(satisfyingSet)



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
maxVelocity = calculateYDragSteps(maxSteps, yBottom, yTop)
print(maxVelocity)
print((maxVelocity * (maxVelocity + 1)) / 2)
