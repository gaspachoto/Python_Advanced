from collections import deque

elves_energies = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]
turns_count = 0
total_energy_spent = 0
total_toys = 0

while boxes and elves_energies:

    while elves_energies and elves_energies[0] < 5:
        elves_energies.popleft()

    if not elves_energies:
        break
    turns_count += 1
    box = boxes.pop()
    elf_energy = elves_energies.popleft()
    if turns_count % 15 == 0 and 2 * box <= elf_energy:
        total_energy_spent += 2 * box
        elves_energies.append(elf_energy - 2 * box)
    elif turns_count % 5 == 0 and box <= elf_energy:
        total_energy_spent += box
        elves_energies.append(elf_energy - box)
    elif turns_count % 3 == 0 and 2 * box <= elf_energy:
        total_toys += 2
        total_energy_spent += 2 * box
        elves_energies.append(elf_energy - 2 * box + 1)
    elif box <= elf_energy and turns_count % 3 != 0:
        total_toys += 1
        total_energy_spent += box
        elves_energies.append(elf_energy - box + 1)
    else:
        boxes.append(box)
        elves_energies.append(elf_energy * 2)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy_spent}")
if elves_energies:
    print(f"Elves left: {', '.join(str(x) for x in elves_energies)}")
if boxes:
    print(f"Boxes left: {', '.join(str(x) for x in boxes)}")

