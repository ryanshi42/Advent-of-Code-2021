class Board:
    def __init__(self, name, rowList):
        self.name = name
        self.rowList = []
        for row in rowList:
            newRow = row.split(' ')
            newRow = [value for value in newRow if value != '']
            self.rowList.append(newRow)

    def checkBoard(self, calledNum):
        self.rowList = [[p if p != calledNum else 'x' for p in s] for s in self.rowList]

    def checkWin(self):
        for row in self.rowList:
            if row == ["x"] * 5:
                return True
        
        for i in range(5):
            j = 0
            for row in self.rowList:
                if row[i] != "x":
                    break
                if j == 4:
                    return True
                j += 1
        
        return False
    
    def sumBoard(self):
        count = 0
        for row in self.rowList:
            for entry in row:
                if entry != "x":
                    count += int(entry)

        return count


with open('day4_1inputNumbers.txt') as f, open('day4_1inputBoards.txt') as g:
    callingList = f.readlines()[0].split(',')
    boardList = ''.join(g.readlines()).split('\n\n')
    boards = []
    i = 1
    for board in boardList:
        print(board)
        boards.append(Board("Board " + str(i), board.split('\n')))
        print()
        i += 1
    for call in callingList:
        # print(call)
        for board in boards:
            board.checkBoard(call)
            if board.checkWin() is True:
                print(board.sumBoard())
                print(call)
                print(int(call) * int(board.sumBoard()))
                exit(0)
        
    