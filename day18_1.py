import math

class Node:
    def __init__(self, parent, left, right, height):
        self.parent = parent
        self.left = left
        self.right = right
        self.height = height

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent

    def getHeight(self):
        return self.height

    def setLeft(self, newValue):
        self.left = newValue
    
    def setRight(self, newValue):
        self.right = newValue

    def setParent(self, newValue):
        self.parent = newValue

    def printNode(self):
        print('[', end='')
        if isinstance(self.left, int):
            print(str(self.left), end='')
        else:
            self.left.printNode()
        print(',', end='')
        if isinstance(self.right, int):
            print(str(self.right), end='')
        else:
            self.right.printNode()
        
        print(']', end='')

        # print('height=' + str(self.height))
    
    def calculateNode(self):
        sum = 0
        if isinstance(self.left, int):
            sum += 3 * self.left
        else:
            sum += 3 * self.left.calculateNode()
        if isinstance(self.right, int):
            sum += 2 * self.right
        else:
            sum += 2 * self.right.calculateNode()
        return sum
            
    def explode(self):
        # parentNode = None
        # hasLeft = False
        # hasRight = False
        # while parentNode is not None and not (hasLeft and hasRight):
        #     parentNode = self.getParent()
        #     if not hasLeft and isinstance(parentNode.getLeft(), int):
        #         hasLeft = True
        #         parentNode.setLeft(parentNode.getLeft() + self.getLeft())
        #     if not hasRight and isinstance(parentNode.getRight(), int):
        #         hasRight = True
        #         parentNode.setRight(parentNode.getRight() + self.getRight())
        #     return

        parentNode = self.parent
        # split left
        x = self
        while parentNode is not None:
            if parentNode.getRight() == x:
                ln = parentNode.getLeft()
                if isinstance(ln, int):
                    parentNode.setLeft(self.left + ln)
                else:
                    while not isinstance(ln.getRight(), int):
                        ln = ln.getRight()
                    ln.setRight(self.left + ln.getRight())
                break
            x = parentNode
            parentNode = parentNode.getParent()

        parentNode = self.parent
        x = self
        # split right
        while parentNode is not None:
            if parentNode.getLeft() == x:
                rn = parentNode.getRight()
                if isinstance(rn, int):
                    parentNode.setRight(self.right + rn)
                else:
                    while not isinstance(rn.getLeft(), int):
                        rn = rn.getLeft()
                    rn.setLeft(self.right + rn.getLeft())
                break
            x = parentNode
            parentNode = parentNode.getParent()
        parentNode = self.parent
        if parentNode.getLeft() == self:
            parentNode.setLeft(0)
        else:
            parentNode.setRight(0)
        return

    def splitLeft(self):
        self.left = Node(self, math.floor(self.left / 2), math.ceil(self.left / 2), self.height + 1)

    def splitRight(self):
        self.right = Node(self, math.floor(self.right / 2), math.ceil(self.right / 2), self.height + 1)

    def incrHeight(self):
        self.height += 1
        if not isinstance(self.left, int):
            self.left.incrHeight()
        if not isinstance(self.right, int):
            self.right.incrHeight()

    def addNode(self, rightNode):
        nn = Node(None, self, rightNode, 0)
        self.setParent(nn)
        rightNode.setParent(nn)
        self.incrHeight()
        rightNode.incrHeight()
        while True:
            if nn.checkExplodeConditions() is True and nn.checkSplitConditions() is True:
                break
            nn.printNode()
            print()

        return nn

    def checkExplodeConditions(self):
        if not isinstance(self.getLeft(), int) and not self.getLeft().checkExplodeConditions():
            return False
        elif self.height >= 4:
            self.explode()
            return False
        elif not isinstance(self.getRight(), int) and not self.getRight().checkExplodeConditions():
            return False
        elif isinstance(self.getLeft(), int) and isinstance(self.getRight(), int):
            return True

        return True

    def checkSplitConditions(self):
        if not isinstance(self.getLeft(), int) and not self.getLeft().checkSplitConditions():
            return False
        elif isinstance(self.getLeft(), int) and self.getLeft() >= 10:
            self.splitLeft()
            return False
        elif isinstance(self.getRight(), int) and self.getRight() >= 10:
            self.splitRight()
            return False
        elif not isinstance(self.getRight(), int) and not self.getRight().checkSplitConditions():
            return False
        elif isinstance(self.getLeft(), int) and isinstance(self.getRight(), int):
            return True
        
        return True

def nodeParse(parent, nodeStr, height):
    leftNode = None
    rightNode = None
    if nodeStr[0] != '[':
        assert(False)
    nn = Node(parent, leftNode, rightNode, height)
    isRight = False
    i = 1
    while i < len(nodeStr):
        if nodeStr[i] == ']':
            break
        elif nodeStr[i] == ' ':
            continue
        elif nodeStr[i] == '\n':
            return i
        elif nodeStr[i] == ',':
            isRight = True
        elif nodeStr[i] == '[':
            k, newNode = nodeParse(nn, nodeStr[i:], height + 1)
            i += (k - 1)
            if not isRight:
                leftNode = newNode
            else:
                rightNode = newNode
        else:
            # is a number
            if not isRight:
                leftNode = int(nodeStr[i])
            else:
                rightNode = int(nodeStr[i])
        i += 1
    i += 1
    nn.setLeft(leftNode)
    nn.setRight(rightNode)

    return i, nn

argList = open('day18_1.in').read().split('\n')

_, startNode = nodeParse(None, argList[0], 0)
print(startNode)
startNode.printNode()
print()

for i in range(1, len(argList)):
    _, nextNode = nodeParse(None, argList[i], 0)
    startNode = startNode.addNode(nextNode)
    startNode.printNode()
    print()
startNode.printNode()
print()
print(startNode.calculateNode())

# _, startNode = nodeParse(None, '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', 0)
# print(startNode)
# startNode.checkConditions()
# startNode.printNode()
# print()


