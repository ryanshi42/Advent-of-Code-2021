argList = []

with open("day8_1input.txt") as f:
    argList = f.readlines()
count = 0
for arg in argList:
    outputList = arg.split(" | ")[1].split(" ")
    print(outputList)
    for output in outputList: 
        if len(output.strip()) in {2, 3, 4, 7}:
            count += 1

print(count)