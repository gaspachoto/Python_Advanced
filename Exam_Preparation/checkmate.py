def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 8

matrix = []

for row in range(size):
    matrix.append(input().split())

d = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up_right": lambda r, c: (r - 1, c + 1),
    "up_left": lambda r, c: (r - 1, c - 1),
    "down_right": lambda r, c: (r + 1, c + 1),
    "down_left": lambda r, c: (r + 1, c - 1),
}

paths = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "Q":
            for direction in d:
                next_row, next_col = d[direction](row, col)
                while is_inside(next_row, next_col, size):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        paths.append([row, col])
                        break
                    next_row, next_col = d[direction](next_row, next_col)

if len(paths) == 0:
    print("The king is safe!")
else:
    print(*paths, sep="\n")
