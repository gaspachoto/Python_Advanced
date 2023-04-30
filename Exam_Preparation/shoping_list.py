def shopping_list(budget, **kwargs):
    products_bought = []
    if budget < 100:
        return f"You do not have enough budget."
    else:
        for product, price in kwargs.items():
            price, quantity = float(price[0]), int(price[1])
            total_price = price * quantity
            if budget > total_price and len(products_bought) < 5:
                budget -= total_price
                products_bought.append(f"You bought {product} for {total_price:.2f} leva.")
    return "\n".join(products_bought)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

