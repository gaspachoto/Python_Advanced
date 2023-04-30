def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


player1, player2 = input().split(", ")
size = 7
matrix = []
player1_points = 501
player2_points = 501
turn = 1
player1_row = 0
player1_col = 0
player2_row = 0
player2_col = 0
player1_turns = 0
player2_turns = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

while True:
    if turn % 2 != 0:
        player1_turns += 1
        player1_hit = input().strip("()").split(', ')
        player1_row, player1_col = int(player1_hit[0]), int(player1_hit[1])
        if is_inside(player1_row, player1_col, size):
            if matrix[player1_row][player1_col] == "D":
                player1_points -= 2 * (int(matrix[player1_row][0]) + int(matrix[player1_row][6])
                + int(matrix[0][player1_col]) + int(matrix[6][player1_col]))
            elif matrix[player1_row][player1_col] == "T":
                player1_points -= 3 * (int(matrix[player1_row][0]) + int(matrix[player1_row][6])
                + int(matrix[0][player1_col]) + int(matrix[6][player1_col]))
            elif matrix[player1_row][player1_col] == "B":
                print(f"{player1} won the game with {player1_turns} throws!")
                break
            else:
                player1_points -= int(matrix[player1_row][player1_col])
            if player1_points <= 0:
                print(f"{player1} won the game with {player1_turns} throws!")
                break

    else:
        player2_turns += 1
        player2_hit = input().strip("()").split(', ')
        player2_row, player2_col = int(player2_hit[0]), int(player2_hit[1])
        if is_inside(player2_row, player2_col, size):
            if matrix[player2_row][player2_col] == "D":
                player2_points -= 2 * (int(matrix[player2_row][0]) + int(matrix[player2_row][6])
                + int(matrix[0][player2_col]) + int(matrix[6][player2_col]))
            elif matrix[player2_row][player2_col] == "T":
                player2_points -= 3 * (int(matrix[player2_row][0]) + int(matrix[player2_row][6])
                + int(matrix[0][player2_col]) + int(matrix[6][player2_col]))
            elif matrix[player2_row][player2_col] == "B":
                print(f"{player2} won the game with {player2_turns} throws!")
                break
            else:
                player2_points -= int(matrix[player2_row][player2_col])
            if player2_points <= 0:
                print(f"{player2} won the game with {player2_turns} throws!")
                break
    turn += 1
