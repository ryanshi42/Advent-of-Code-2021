from collections import Counter

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
C1 = Counter()

for i in range(1, len(ss)):
    C1[ss[i - 1] + ss[i]] += 1

print(C1)

for _ in range(40):
    C2 = Counter()
    for i in C1.keys():
        toInsert = pairRules[i]
        C2[i[0] + toInsert] += C1[i]
        C2[toInsert + i[1]] += C1[i]
    C1 = C2

C3 = Counter()
for k in C1.keys():
    C3[k[0]] += C1[k]
C3[ss[-1]] += 1
# print(ss)
print(max(C3.values()) - min(C3.values()))