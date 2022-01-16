with open('day2_1input.txt') as f:
    argList = f.readlines()
    horizontalPos = 0
    curDepth = 0
    curAim = 0
    for arg in argList:
        commandList = arg.split(" ")
        if commandList[0] == "forward":
            horizontalPos += int(commandList[1])
            curDepth += curAim * int(commandList[1])
        if commandList[0] == "up":
            curAim -= int(commandList[1])
        if commandList[0] == "down":
            curAim += int(commandList[1])
    print("multiplier = " + str(curDepth * horizontalPos))