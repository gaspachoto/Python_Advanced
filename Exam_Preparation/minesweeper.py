def near_bomb(row, col, matrix):
    number = 0
    if is_inside(row - 1, col, size):
        if matrix[row - 1][col] == "*":
            number += 1
    if is_inside(row + 1, col, size):
        if matrix[row + 1][col] == "*":
            number += 1
    if is_inside(row, col - 1, size):
        if matrix[row][col - 1] == "*":
            number += 1
    if is_inside(row, col + 1, size):
        if matrix[row][col + 1] == "*":
            number += 1
    if is_inside(row - 1, col - 1, size):
        if matrix[row - 1][col - 1] == "*":
            number += 1
    if is_inside(row - 1, col + 1, size):
        if matrix[row - 1][col + 1] == "*":
            number += 1
    if is_inside(row + 1, col - 1, size):
        if matrix[row + 1][col - 1] == "*":
            number += 1
    if is_inside(row + 1, col + 1, size):
        if matrix[row + 1][col + 1] == "*":
            number += 1
    return number


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
number_of_bombs = int(input())

matrix = []

for row in range(size):
    row_elements = []
    for col in range(size):
        row_elements.append("0")
    matrix.append(row_elements)
for _ in range(number_of_bombs):
    bombs_coordinates = (input().strip("()").split(", "))
    bomb_row, bomb_col = int(bombs_coordinates[0]), int(bombs_coordinates[1])
    matrix[bomb_row][bomb_col] = "*"

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "*":
            continue
        else:
            matrix[row][col] = str(near_bomb(row, col, matrix))

for row in matrix:
    print(f"{' '.join(row)}")