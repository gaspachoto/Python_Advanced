def is_inside(trow_row, trow_col, matrix):
    return 0 <= trow_row < len(matrix) and 0 <= trow_col < len(matrix)


def hit_points(trow_row, trow_col, matrix):
    size = len(matrix)
    points = 0
    if matrix[trow_row][trow_col] == "D":
        points = 2 * (int(matrix[trow_row][0]) + int(matrix[trow_row][size - 1]) + int(matrix[0][trow_col]) + int(
            matrix[size - 1][trow_col]))
        return points
    elif matrix[trow_row][trow_col] == "T":
        points = 3 * (int(matrix[trow_row][0]) + int(matrix[trow_row][size - 1]) + int(matrix[0][trow_col]) + int(
            matrix[size - 1][trow_col]))
        return points
    elif matrix[trow_row][trow_col] == "B":
        points = 501
        return points
    else:
        points = int(matrix[trow_row][trow_col])
        return points


player_one, player_two = input().split(", ")

size = 7
matrix = []
for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

points_dict = {
    player_one: 501,
    player_two: 501
}
turns_dict = {
    player_one: 0,
    player_two: 0
}

winner = ""
current_player, other_player = player_one, player_two
while True:
    coordinates = input().strip("()").split(", ")
    turns_dict[current_player] += 1
    trow_row = int(coordinates[0])
    trow_col = int(coordinates[1])
    if is_inside(trow_row, trow_col, matrix):
        points_to_be_deduced = hit_points(trow_row, trow_col, matrix)
        points_dict[current_player] -= points_to_be_deduced
    if points_dict[current_player] <= 0:
        winner = current_player
        break
    current_player, other_player = other_player, current_player

print(f"{winner} won the game with {turns_dict[current_player]} throws!")
