argList = []
pairRules = {}

ss = ""

with open('day14_1.in') as f:
    argList = f.readlines()

for arg in argList:
    if '->' in arg:
        pairRules[arg.strip().split('->')[0][:-1]] = arg.strip().split('->')[1][1:]
    elif arg == '\n':
        pass
    else:
        ss = arg.strip()

print(ss)
# print(pairRules)

for k in range(40):
    newString = ''
    for i in range(1, len(ss)):
        toInsert = pairRules[ss[i - 1] + ss[i]]
        newString += ss[i - 1]
        newString += toInsert
    newString += ss[-1]
    ss = newString

# print(ss)

lettersDict = {}
for elem in ss:
    lettersDict[elem] = lettersDict.get(elem, 0) + 1
print(max(lettersDict.values()) - min(lettersDict.values()))