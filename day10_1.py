import math

def isClose(symbol):
    return symbol in {'}', ')', ']', '>'}

def score(symbol):
    if symbol == ')':
        return 3
    elif symbol == ']':
        return 57
    elif symbol == '}':
        return 1197
    elif symbol == '>': 
        return 25137
    else:
        return 0

def part2Score(symbol):
    if symbol == '(':
        return 1
    elif symbol == '[':
        return 2
    elif symbol == '{':
        return 3
    elif symbol == '<': 
        return 4
    else:
        return 0

def doesMatch(s1, s2):
    if s1 == '(' and s2 == ')':
        return True
    elif s1 == '{' and s2 == '}':
        return True
    elif s1 == '<' and s2 == '>':
        return True
    elif s1 == '[' and s2 == ']':
        return True
    return False

argList = []

with open('day10_1.in') as f:
    argList = f.readlines()
    # print(argList)
# argList = ['<{([{{}}[<[[[<>{}]]]>[]]\n']

currStack = []
currScore = 0
burrScore = 0
burrScoreList = []
for line in argList:
    burrScore = 0
    currStack = []
    i = 0
    incomplete = True
    nextChar = line[i]
    while nextChar != '\n':
        if isClose(nextChar):
            if not doesMatch(currStack.pop(), nextChar):
                currScore += score(nextChar)
                incomplete = False
                break
        else:
            currStack.append(nextChar)
        i += 1
        if i == len(line):
            break
        nextChar = line[i]
    
    if incomplete is True:
        currStack.reverse()
        for symbol in currStack:
            burrScore *= 5
            burrScore += part2Score(symbol)
        burrScoreList.append(burrScore)
burrScoreList.sort()
print(burrScoreList)
print(burrScoreList.pop(math.floor(len(burrScoreList)/2)))
# stack = "<[{("

