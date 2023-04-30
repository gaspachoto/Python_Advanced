def stock_availability(items, sell_dell, *args):
    if sell_dell == "delivery":
        for item in args:
            items.append(item)
    elif sell_dell == "sell":
        if args:
            for arg in args:
                if str(arg).isdigit():
                    for i in range(arg):
                        if len(items) > 0:
                            items.pop(0)
                else:
                    if arg in items:
                        while arg in items:
                            items.remove(arg)
        else:
            items.pop(0)
    return items


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
