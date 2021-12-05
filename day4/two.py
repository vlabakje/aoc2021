class Board:
    def __init__(self, board):
        self._board = []
        self._marked = set()
        self._all = set()
        for row in board.split("\n"):
            if row != "":
                self._board.append([int(i) for i in row.split(" ") if i != ""])
                assert len(self._board[-1]) == 5
                self._all |= set(self._board[-1])
        assert len(self._board) == 5

    def on_drawn(self, drawn):
        if drawn in self._all:
            self._marked.add(drawn)
        return self.has_bingo()
    
    def has_bingo(self):
        for row in self._board:
            if all(cell in self._marked for cell in row):
                return True
        for col in range(len(self._board[0])):
            if all(row[col] in self._marked for row in self._board):
                return True
        return False

    def remaining(self):
        return sum(self._all) - sum(self._marked)

def main():
    draw, boards = draw_boards()
    for drawn in draw:
        if len(boards) == 1:
            if boards[0].on_drawn(drawn):
                return boards[0].remaining() * drawn
        else:
            for board in boards[:]:
                if board.on_drawn(drawn):
                    boards.remove(board)

def draw_boards():
    with open("input") as fileh:
        contents = fileh.read().split("\n\n")
        draw = list(map(int, contents.pop(0).split(",")))
        boards = [Board(board) for board in contents]
        return draw, boards

if __name__ == "__main__":
    print(main())
