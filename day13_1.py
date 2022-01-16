argList = []
foldList = []

class Paper:
    def __init__(self, dotList):
        self.dotList = dotList

    def getDotList(self):
        return self.dotList

    def fold(self, axis, line):
        line = int(line)
        newDotSet = set()
        if axis == 'x':
            # fold left
            for dot in self.dotList:
                if dot[0] < line:
                    newDotSet.add(dot)
                else:
                    newDotSet.add((line * 2 - dot[0], dot[1]))
        elif axis == 'y':
            # fold up
            for dot in self.dotList:
                if dot[1] < line:
                    newDotSet.add(dot)
                else:
                    newDotSet.add((dot[0], line * 2 - dot[1]))
        return Paper(list(newDotSet))
    
    def numDots(self):
        return len(self.dotList)

with open('day13_1.in') as f:
    argList = [(int(row.strip().split(',')[0]), int(row.strip().split(',')[1])) for row in f.readlines()]

with open('day13_1fold.in') as f:
    foldList = [(row[11:].strip().split('=')[0], row[11:].strip().split('=')[1]) for row in f.readlines()]

print(argList)
print(foldList)
newPaper = Paper(argList)
for fold in foldList:
    newPaper = newPaper.fold(fold[0], int(fold[1]))
print(newPaper.numDots())

for i in range(50):
    for j in range(50):
        if (i, j) in newPaper.getDotList():
            print('#', end='')
        else:
            print('.', end='')
    print()
    