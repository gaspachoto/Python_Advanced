from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
products_made = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}
succeeded = False

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    current_sum = material + magic_level
    if current_sum < 100:
        if current_sum % 2 == 0:
            material *= 2
            magic_level *= 3
            current_sum = material + magic_level
        else:
            current_sum *= 2
    if current_sum > 499:
        current_sum /= 2
    if 100 <= current_sum < 200:
        products_made['Gemstone'] += 1
    elif 200 <= current_sum < 300:
        products_made['Porcelain Sculpture'] += 1
    elif 300 <= current_sum < 400:
        products_made['Gold'] += 1
    elif 400 <= current_sum < 500:
        products_made['Diamond Jewellery'] += 1
if products_made['Gemstone'] > 0 and products_made['Porcelain Sculpture'] > 0\
        or products_made['Gold'] > 0 and products_made['Diamond Jewellery'] > 0:
    succeeded = True
if succeeded:
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for key, value in sorted(products_made.items()):
    if value > 0:
        print(f"{key}: {value}")
