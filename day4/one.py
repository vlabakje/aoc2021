def main():
    draw, boards = draw_boards()
    #print(f"{draw=}\n\n {boards=}")
    for i in range(1, len(draw)):
        draw_set = set(draw[:i])
        for board in boards:
            if wins(draw_set, board):
                #print(f"winner {draw_set=} {board=}")
                return score(draw_set, board, draw[i-1])


def wins(draw_set, board):
    for row in board:
        if all(cell in draw_set for cell in row):
            return True
    for col in range(len(board[0])):
        if all(row[col] in draw_set for row in board):
            return True
    return False


def score(draw_set, board, final_draw):
    result = 0
    for row in board:
        result += sum(cell for cell in row if cell not in draw_set)
    #print(f"{result=} {final_draw=}")
    return result * final_draw


def draw_boards():
    with open("input") as fileh:
        contents = fileh.read().split("\n\n")
        draw = list(map(int, contents.pop(0).split(",")))
        boards = []
        for b in contents:
            board = []
            for row in b.split("\n"):
                if row != "":
                    board.append([int(i) for i in row.split(" ") if i != ""])
                    assert len(board[-1]) == 5
            assert len(board) == 5
            boards.append(board)
        return draw, boards


if __name__ == "__main__":
    print(main())
