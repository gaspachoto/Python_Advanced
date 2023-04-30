def get_next_position(row, col, direction):
    if direction == "up":
        if is_inside(row - 1, col, size):
            return row - 1, col
        else:
            return 5, col
    if direction == "down":
        if is_inside(row + 1, col, size):
            return row + 1, col
        else:
            return 0, col
    if direction == "left":
        if is_inside(row, col - 1, size):
            return row, col - 1
        else:
            return row, 5
    if direction == "right":
        if is_inside(row, col + 1, size):
            return row, col + 1
        else:
            return row, 0


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 6
matrix = []
rover_col = 0
rover_row = 0
water_found = 0
metal_found = 0
concrete_found = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            rover_row = row
            rover_col = col
    matrix.append(row_elements)

directions = input().split(", ")

for direction in directions:
    rover_row, rover_col = get_next_position(rover_row, rover_col, direction)
    if matrix[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    elif matrix[rover_row][rover_col] == "W":
        water_found += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "M":
        metal_found += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")
    elif matrix[rover_row][rover_col] == "C":
        concrete_found += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")

if water_found > 0 and metal_found > 0 and concrete_found > 0:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
