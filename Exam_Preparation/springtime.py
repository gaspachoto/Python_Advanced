def start_spring(**kwargs):
    collection = {}
    for key, value in kwargs.items():
        collection[value] = []
    for key, value in kwargs.items():
        collection[value].append(key)
    sorted_collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for types, items in sorted_collection:
        result.append(f'{types}:')
        for item in sorted(items):
            result.append(f'-{item}')
    return "\n".join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))


