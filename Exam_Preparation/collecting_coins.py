from math import floor


def get_next_position(row, col, direction):
    if direction == "up":
        if is_inside(row - 1, col, size):
            return row - 1, col
        else:
            return size - 1, col
    if direction == "down":
        if is_inside(row + 1, col, size):
            return row + 1, col
        else:
            return 0, col
    if direction == "left":
        if is_inside(row, col - 1, size):
            return row, col - 1
        else:
            return row, size - 1
    if direction == "right":
        if is_inside(row, col + 1, size):
            return row, col + 1
        else:
            return row, 0


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = []
player_row = 0
player_col = 0
collected_coins = 0
player_path = []
won = False

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "P":
            player_row, player_col = row, col
    matrix.append(row_elements)
player_path.append([player_row, player_col])
matrix[player_row][player_col] = '0'
while True:
    direction = input()
    if direction not in ['up', 'down', 'left', 'right']:
        continue
    player_row, player_col = get_next_position(player_row, player_col, direction)
    player_path.append([player_row, player_col])
    if matrix[player_row][player_col] == "X":
        collected_coins = collected_coins / 2
        break
    else:
        collected_coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = '0'
        if collected_coins >= 100:
            won = True
            break

if won:
    print(f"You won! You've collected {floor(collected_coins)} coins.")
else:
    print(f"Game over! You've collected {floor(collected_coins)} coins.")
print(f"Your path:")
for path in player_path:
    print(path)
