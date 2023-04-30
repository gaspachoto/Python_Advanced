from collections import deque

fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_powers = [int(x) for x in input().split(', ')]
enough_fireworks = False
fireworks_made = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

while fireworks_effects and explosive_powers:
    fireworks_effect = fireworks_effects.popleft()
    explosive_power = explosive_powers.pop()
    if fireworks_effect <= 0:
        explosive_powers.append(explosive_power)
        continue
    if explosive_power <= 0:
        fireworks_effects.appendleft(fireworks_effect)
        continue
    value = fireworks_effect + explosive_power
    if value % 3 == 0 and value % 5 != 0:
        fireworks_made['Palm Fireworks'] += 1
    elif value % 5 == 0 and value % 3 != 0:
        fireworks_made['Willow Fireworks'] += 1
    elif value % 3 == 0 and value % 5 == 0:
        fireworks_made['Crossette Fireworks'] += 1
    else:
        fireworks_effect -= 1
        fireworks_effects.append(fireworks_effect)
        explosive_powers.append(explosive_power)
    if fireworks_made['Palm Fireworks'] >= 3 and fireworks_made['Willow Fireworks'] >= 3\
            and fireworks_made['Crossette Fireworks'] >= 3:
        enough_fireworks = True
        break

if enough_fireworks:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")
for key, value in fireworks_made.items():
    print(f"{key}: {value}")
