from collections import deque


def shopping_cart(*args):
    meals_dict = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }
    commands = deque(args)
    while commands:
        command = commands.popleft()
        if command == "Stop":
            break
        meal, product = command[0], command[1]
        if meal == "Pizza" and product not in meals_dict['Pizza'] and len(meals_dict['Pizza']) < 4:
            meals_dict['Pizza'].append(product)
        elif meal == 'Soup' and product not in meals_dict['Soup'] and len(meals_dict['Soup']) < 3:
            meals_dict['Soup'].append(product)
        elif meal == "Dessert" and product not in meals_dict['Dessert'] and len(meals_dict['Dessert']) < 2:
            meals_dict['Dessert'].append(product)
    result = []
    sorted_meals_dict = sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    for meals, products in sorted_meals_dict:
        result.append(f'{meals}:')
        for product in sorted(products):
            result.append(f' - {product}')
    if meals_dict['Soup'] or meals_dict['Pizza'] or meals_dict['Dessert']:
        return "\n".join(result)
    else:
        return f"No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
