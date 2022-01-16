class Prism:
    def __init__(self, xa, xb, ya, yb, za, zb):
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb
        self.za = za
        self.zb = zb
    
    def contains(self, other):
        return (self.xa <= other.xa and
        self.xb >= other.xb and
        self.ya <= other.ya and
        self.yb >= other.yb and
        self.za <= other.za and
        self.zb >= other.zb)

    def intersects(self, other):
        return (self.xa < other.xb and 
        self.xb > other.xa and
        self.ya < other.yb and
        self.yb > other.ya and
        self.za < other.zb and
        self.zb > other.za)

    def getSize(self):
        return (self.xb - self.xa) * (self.yb - self.ya) * (self.zb - self.za)

    # Other = off, self = on
    def newPrism(self, other):
        if other.contains(self):
            return []
        elif not other.intersects(self):
            return [self]
        
        # here, there is an intersection
        xs = sorted((self.xa, self.xb, other.xa, other.xb))
        ys = sorted((self.ya, self.yb, other.ya, other.yb))
        zs = sorted((self.za, self.zb, other.za, other.zb))

        ret = []
        for x0, x1 in zip(xs, xs[1:]):
            for y0, y1 in zip(ys, ys[1:]):
                for z0, z1 in zip(zs, zs[1:]):
                    p = Prism(x0, x1, y0, y1, z0, z1)
                    if self.contains(p) and not other.intersects(p):
                        ret.append(p)
        return ret




rebootList = []

rebootList = open('day22_1.in').read().strip().split('\n')

for i in range(-100000, 100000):
    for j in range(-100000, 100000):
        for k in range(-100000, 100000):
            bootSet.add((i,j,k))

prismList = []

for w in range(len(rebootList)):
    print(w)
    reboot = rebootList[w].strip()
    on = False
    newStr = ''
    if reboot[:2] == 'on':
        on = True
        newStr = reboot[3:]
    else:
        newStr = reboot[4:]
    
    xCoord, yCoord, zCoord = newStr.split(',')
    xa = int(xCoord[2:].split('..')[0])
    xb = int(xCoord[2:].split('..')[1]) + 1
    ya = int(yCoord[2:].split('..')[0])
    yb = int(yCoord[2:].split('..')[1]) + 1
    za = int(zCoord[2:].split('..')[0])
    zb = int(zCoord[2:].split('..')[1]) + 1
    np = Prism(xa, xb, ya, yb, za, zb)
    npl = []
    for prism in prismList:
        npl += prism.newPrism(np)

    if on:
        npl.append(np)
    # print(npl)
    prismList = npl
    

print(sum([p.getSize() for p in prismList]))

    # newBootSet = bootSet
    # for t in bootSet:
    #     i = t[0]
    #     j = t[1]
    #     k = t[2]
    #     if i in range(xa, xb + 1) and j in range(ya, yb + 1) and k in range(za, zb + 1):
    #         if on:
    #             newBootSet.discard(t)
    #             defsOn.add(t)
    #         else:
    #             newBootSet.discard(t)
    #             defsOff.add(t)