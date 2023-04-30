def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_next_position(row, col, direction):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


initial_str = input()
size = int(input())
matrix = []
player_row = 0
player_col = 0
final_str = initial_str

for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == "P":
            player_row, player_col = row, col
    matrix.append(row_elements)

matrix[player_row][player_col] = "-"

number_of_directions = int(input())

for _ in range(number_of_directions):
    direction = input()
    next_row, next_col = get_next_position(player_row, player_col, direction)
    if is_inside(next_row, next_col, size):
        player_row, player_col = next_row, next_col
        if matrix[player_row][player_col] == "-":
            matrix[player_row][player_col] = "P"
        else:
            final_str += matrix[player_row][player_col]
        matrix[player_row][player_col] = "-"
    else:
        if len(final_str) > 0:
            final_str = final_str[:-1]

matrix[player_row][player_col] = "P"
print(final_str)
for row in matrix:
    print(*row, sep="")
