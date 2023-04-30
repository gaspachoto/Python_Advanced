from collections import deque


def best_list_pureness(list, rotations):
    pureness = 0
    rotation = 0
    list = deque(list)
    for index in range(len(list)):
        pureness += list[index] * index
    best_pureness = pureness
    best_rotation = rotation
    pureness = 0
    for i in range(rotations):
        rotation += 1
        last = list.pop()
        list.appendleft(last)
        for index in range(len(list)):
            pureness += list[index] * index
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation
        pureness = 0
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)









