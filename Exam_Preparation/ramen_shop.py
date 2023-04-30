from collections import deque

ramen_bowls = deque([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while ramen_bowls and customers:
    ramen = ramen_bowls.pop()
    customer = customers.popleft()
    if ramen > customer:
        ramen -= customer
        ramen_bowls.append(ramen)
    elif ramen < customer:
        customer -= ramen
        customers.appendleft(customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
