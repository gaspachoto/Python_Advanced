def get_next_position(row, col, direction, steps, rows, cols):
    if direction == "up":
        if is_inside(row - 1, col, rows, cols):
            return row - 1, col
        else:
            return rows - 1, col
    if direction == "down":
        if is_inside(row + 1, col, rows, cols):
            return row + 1, col
        else:
            return 0, col
    if direction == "left":
        if is_inside(row, col - 1, rows, cols):
            return row, col - 1
        else:
            return row, cols - 1
    if direction == "right":
        if is_inside(row, col + 1, rows, cols):
            return row, col + 1
        else:
            return row, 0


def is_inside(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


rows, cols, = [int(x) for x in input().split(', ')]
matrix = []
position_row = 0
position_col = 0
collected_items = {'Christmas decorations': 0, 'Gifts': 0, 'Cookies': 0}
total_items = 0
all_items_collected = False
for row in range(rows):
    row_elements = input().split()
    for col in range(cols):
        if row_elements[col] == "Y":
            position_row, position_col = row, col
        if row_elements[col] == "D" or row_elements[col] == "G" or row_elements[col] == "C":
            total_items += 1
    matrix.append(row_elements)

matrix[position_row][position_col] = "x"

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split('-')
    direction = current_command[0]
    steps = int(current_command[1])
    for step in range(steps):
        position_row, position_col = get_next_position(position_row, position_col, direction, steps, rows, cols)
        if matrix[position_row][position_col] == "D":
            total_items -= 1
            collected_items['Christmas decorations'] += 1
        if matrix[position_row][position_col] == "G":
            total_items -= 1
            collected_items['Gifts'] += 1
        if matrix[position_row][position_col] == "C":
            total_items -= 1
            collected_items['Cookies'] += 1
        matrix[position_row][position_col] = "x"
        if total_items == 0:
            all_items_collected = True
            break
    if all_items_collected:
        break

matrix[position_row][position_col] = "Y"
if all_items_collected:
    print(f"Merry Christmas!")
print(f"You've collected:")
for key, value in collected_items.items():
    print(f'- {value} {key}')
for row in matrix:
    print(*row, sep=' ')
