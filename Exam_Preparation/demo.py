def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def move_white(row, col, size):
    return row - 1, col


def move_black(row, col, size):
    return row + 1, col


size = 8
matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "w":
            white_row = row
            white_col = col
        if row_elements[col] == "b":
            black_row = row
            black_col = col
    matrix.append(row_elements)

pawn_field_matrix = [
    ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
    ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
    ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
    ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
    ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
    ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
    ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
]

turns = 1
while True:
    if turns % 2 != 0:
        if matrix[white_row - 1][white_col - 1] == "b" and is_inside(white_row - 1, white_col - 1, size):
            print(f"Game over! White win, capture on {pawn_field_matrix[white_row - 1][white_col - 1]}.")
            break
        elif matrix[white_row - 1][white_col + 1] == "b" and is_inside(white_row - 1, white_col + 1, size):
            print(f"Game over! White win, capture on {pawn_field_matrix[white_row - 1][white_col + 1]}.")
            break
        white_row, white_col = move_white(white_row, white_col, size)
        if white_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {pawn_field_matrix[white_row][white_col]}.")
            break
        matrix[white_row][white_col] = "w"
    if turns % 2 == 0:
        if matrix[black_row + 1][black_col - 1] == "w" and is_inside(black_row + 1, black_col - 1, size):
            print(f"Game over! Black win, capture on {pawn_field_matrix[black_row + 1][black_col - 1]}.")
            break
        elif matrix[black_row + 1][black_col + 1] == "w" and is_inside(black_row + 1, black_col + 1, size):
            print(f"Game over! Black win, capture on {pawn_field_matrix[black_row + 1][black_col + 1]}.")
            break
        black_row, black_col = move_black(black_row, black_col, size)
        if black_row == 7:
            print(f"Game over! Black pawn is promoted to a queen at {pawn_field_matrix[black_row][black_col]}.")
            break
        matrix[black_row][black_col] = "b"
    turns += 1
