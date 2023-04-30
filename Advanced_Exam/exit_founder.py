first_player_name, second_player_name = input().split(", ")
size = 6
matrix = []
turns = 0
for row in range(size):
    matrix.append(input().split())

first_player_row = 0
first_player_col = 0
second_player_row = 0
second_player_col = 0
first_player_turn_is_ignored = False
second_player_turn_is_ignored = False

while True:
    turns += 1
    if turns % 2 != 0:
        if first_player_turn_is_ignored:
            first_player_row, first_player_col = [int(x) for x in input().strip("()").split(", ")]
            first_player_turn_is_ignored = False
            continue
        first_player_row, first_player_col = [int(x) for x in input().strip("()").split(", ")]
        if matrix[first_player_row][first_player_col] == "E":
            print(f"{first_player_name} found the Exit and wins the game!")
            break
        elif matrix[first_player_row][first_player_col] == "T":
            print(f"{first_player_name} is out of the game! The winner is {second_player_name}.")
            break
        elif matrix[first_player_row][first_player_col] == "W":
            first_player_turn_is_ignored = True
            print(f"{first_player_name} hits a wall and needs to rest.")
    else:
        if second_player_turn_is_ignored:
            second_player_row, second_player_col = [int(x) for x in input().strip("()").split(", ")]
            second_player_turn_is_ignored = False
            continue
        second_player_row, second_player_col = [int(x) for x in input().strip("()").split(", ")]
        if matrix[second_player_row][second_player_col] == "E":
            print(f"{second_player_name} found the Exit and wins the game!")
            break
        elif matrix[second_player_row][second_player_col] == "T":
            print(f"{second_player_name} is out of the game! The winner is {first_player_name}.")
            break
        elif matrix[second_player_row][second_player_col] == "W":
            second_player_turn_is_ignored = True
            print(f"{second_player_name} hits a wall and needs to rest.")
