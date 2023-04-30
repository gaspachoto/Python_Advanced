from collections import deque

orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]
total_pizzas = 0
all_orders_completed = False

while orders and employees:
    order = orders.popleft()
    if order <= 0 or order > 10:
        continue
    else:
        employee = employees.pop()
        if employee >= order:
            total_pizzas += order
        else:
            order -= employee
            total_pizzas += employee
            orders.appendleft(order)

if not orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")
