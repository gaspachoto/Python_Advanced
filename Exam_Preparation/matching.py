from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue
    if male % 25 == 0 and male != 0:
        males.pop()
        females.appendleft(female)
        continue
    if female % 25 == 0 and female != 0:
        females.popleft()
        males.append(male)
        continue
    if male == female:
        matches += 1
    else:
        male -= 2
        males.append(male)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")
