def naughty_or_nice_list(kids, *args, **kwargs):
    nice_kids = []
    naughty_kids = []

    for command in args:
        number, status = command.split("-")
        number = int(number)
        name = None
        exists = False
        for kid_number, kid_name in kids:
            if number == kid_number and exists:
                exists = False
                break
            if number == kid_number:
                name = kid_name
                exists = True
        if exists:
            kids.remove((number, name))
            if status == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    for name, status in kwargs.items():
        exists = False
        number = None
        for kid_number, kid_name in kids:
            if name == kid_name and exists:
                exists = False
                break
            if name == kid_name:
                exists = True
                number = kid_number

        if exists:
            kids.remove((number, name))
            if status == "Nice":
                nice_kids.append(name)
            else:
                naughty_kids.append(name)

    not_found = [name for number, name in kids]
    result = ""
    if nice_kids:
        result += f"Nice: {', '.join(nice_kids)}\n"
    if naughty_kids:
        result += f"Naughty: {', '.join(naughty_kids)}\n"
    if not_found:
        result += f"Not found: {', '.join(not_found)}\n"
    return result.strip()


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
