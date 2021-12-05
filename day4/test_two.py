from two import Board

BOARD_1_25 = """
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
""".lstrip()


def test_simpleboard():
    board = Board(BOARD_1_25)
    assert not board.has_bingo()
    for drawn in range(1, 6):
        board.on_drawn(drawn)
    assert board.has_bingo()
    assert board.remaining() == 310


def test_simpleboard_vertical():
    board = Board(BOARD_1_25)
    assert not board.has_bingo()
    for drawn in (5, 10, 15, 20, 25):
        board.on_drawn(drawn)
    assert board.has_bingo()
    assert board.remaining() == 250


def test_simpleboard_all_drawn():
    board = Board(BOARD_1_25)
    assert not board.has_bingo()
    for drawn in range(1, 26):
        board.on_drawn(drawn)
    assert board.has_bingo()
    assert board.remaining() == 0


def test_simpleboard_all_drawn():
    board = Board(BOARD_1_25)
    assert not board.has_bingo()
    for drawn in (2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24):
        board.on_drawn(drawn)
    assert not board.has_bingo()
    board.on_drawn(13)
    assert board.has_bingo()
