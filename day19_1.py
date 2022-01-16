scannerList = open('day19_1.in').read().split('\n\n')
readingList = []
for i, scanner in enumerate(scannerList):
    readingList.append(scanner.split('\n')[1:])

def compareBeacons(i, j):
    o1 = readingList[i]
    o2 = readingList[j]
    o1Beacons = []
    overlappingBeacons = []
    obset = set()
    for x in range(len(o1)):
        for y in range(len(o1)):
            if x <= y:
                continue
            x1, y1, z1 = o1[x].split(',')
            x2, y2, z2 = o1[y].split(',')
            diffx = abs(x1) - abs(x2)
            diffy = abs(y1) - abs(y2)
            diffz = abs(z1) - abs(z2)
            o1Beacons.append((x, y, diffx, diffy, diffz))
    for x in range(len(o2)):
        for y in range(len(o2)):
            if x <= y:
                continue
            x1, y1, z1 = o2[x].split(',')
            x2, y2, z2 = o2[y].split(',')
            diffx = abs(x1) - abs(x2)
            diffy = abs(y1) - abs(y2)
            diffz = abs(z1) - abs(z2)
            bset = set(abs(diffx), abs(diffy), abs(diffz))    

            for b in o1Beacons:
                if bset == set(abs(b[2]), abs(b[3]), abs(b[4])):
                    overlappingBeacons.append((b[0],b[1],x,y))
                    obset.add(b[0], b[1])
                    if len(overlappingBeacons) == 12:
                        return overlappingBeacons
    return None


print(readingList[0])
for i in range(len(readingList)):
    for j in range(len(readingList)):
        if j <= i:
            continue
        ob = compareBeacons(i, j)
        if ob is None:
            continue


# idea:

# while bad scanners exist,
# compare with a good scanner
# vote on a correct distance
# if more than 12 votes, pass that distance.

# eventually all scanners are good