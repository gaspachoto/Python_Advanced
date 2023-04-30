from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]
created_bombs = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}
job_done = False

while bomb_effects and bomb_casings:
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()
    bomb_sum = bomb_effect + bomb_casing
    if bomb_sum == 40:
        created_bombs['Datura Bombs'] += 1
    elif bomb_sum == 60:
        created_bombs['Cherry Bombs'] += 1
    elif bomb_sum == 120:
        created_bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effects.appendleft(bomb_effect)
        bomb_casings.append(bomb_casing - 5)
    if created_bombs['Cherry Bombs'] >= 3 and created_bombs['Datura Bombs'] >= 3 and created_bombs['Smoke Decoy Bombs'] >= 3:
        job_done = True
        print(f"Bene! You have successfully filled the bomb pouch!")
        break

if not job_done:
    print(f"You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print(f"Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print(f"Bomb Casings: empty")
for key, value in created_bombs.items():
    print(f"{key}: {value}")
