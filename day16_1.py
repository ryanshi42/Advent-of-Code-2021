class Packet:
    versionSum = 0
    packets = []

    def __init__(self, bitString):
        self.bitString = bitString
    
    def getType(self):
        return int(self.bitString[3:6], 2)

    def getVersion(self):
        return int(self.bitString[:3], 2)
    
    def getVSum(self):
        return self.versionSum

    def processSeq(self, counter):
        i = counter
        # while i + 7 < len(self.bitString):
            # start of next packet
        packetStart = i
        self.versionSum += int(self.bitString[i:i+3], 2) 
        print(int(self.bitString[i:i+3], 2) )
        i += 3
        packetType = int(self.bitString[i:i+3], 2) 
        # print(self.bitString[i:i+3])
        i += 3
        if packetType == 4:
            # literal value
            litBin = ''

            while self.bitString[i] != '0':
                litBin += self.bitString[i + 1 : i + 5]
                i += 5
            litBin += self.bitString[i + 1 : i + 5]
            i += 5
            litValue = int(litBin, 2)

            # Get rid of 0 padding
            # difference = (i - packetStart + 1) % 4
            # i += difference
        else:
            # operator
            i += 1

            if int(self.bitString[i - 1], 2) == 1:
                subpacketNum = int(self.bitString[i : i + 11], 2)
                print(self.bitString[i : i + 11])
                i += 11
                print(self.bitString[i:])
                for _ in range(subpacketNum):
                    i = self.processSeq(i)
                return i
            elif int(self.bitString[i - 1], 2) == 0:
                subpacketLength = int(self.bitString[i : i + 15], 2)
                i += 15
                j = i
                while i + subpacketLength > j:
                    j = self.processSeq(j)
                    print(self.bitString[j:])
                return i + subpacketLength
                
        # print(self.bitString[i:])
        return i

        # BIG NOTE: getting rid of the while loop somehow helped?
        # because when processing for oneself, it was entering an infinite loop where it would never return anything?
            

class Operator(Packet):
    def __init__(self, bitString):
        self.bitString = bitString


hexList = '''
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
'''
hexDict = {}
for hex in hexList.strip().split('\n'):
    hexDict[hex.strip().split(' = ')[0]] = hex.strip().split(' = ')[1]

# print(hexDict)

hexseq = open('day16_1.in').read().strip()
binseq = ''

for bit in hexseq:
    binseq += hexDict[bit]

# binseq = '11101110000000001101010000001100100000100011000001100000'
# binseq = '00111000000000000110111101000101001010010001001000000000'
print(binseq)

fullPacket = Packet(binseq)
fullPacket.processSeq(0)
print(fullPacket.getVSum())