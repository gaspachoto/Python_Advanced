def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 6
matrix = []
points_scored = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

for balls in range(3):
    ball = input().strip("()").split(', ')
    row, col = int(ball[0]), int(ball[1])
    if not is_inside(row, col, size) or matrix[row][col] != "B":
        continue
    else:
        matrix[row][col] = '0'
        points_scored += int(matrix[0][col]) + int(matrix[1][col]) + int(matrix[2][col])\
                      + int(matrix[3][col]) + int(matrix[4][col]) + int(matrix[5][col])

if points_scored < 100:
    print(f"Sorry! You need {100 - points_scored} points more to win a prize.")
elif 100 <= points_scored < 200:
    print(f"Good job! You scored {points_scored} points, and you've won Football.")
elif 200 <= points_scored < 300:
    print(f"Good job! You scored {points_scored} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points_scored} points, and you've won Lego Construction Set.")
