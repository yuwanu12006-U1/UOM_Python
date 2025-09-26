sandwich_orders = ['egg', 'cheese', 'pastrami','pastrami', 'salmon', 'butter with seeni', 'pastrami', 'egg', 'jam']
finished_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("We ran out of pastrami!!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for _ in range(len(sandwich_orders)):
    for order in sandwich_orders:
        print(f"I made your {order.title()} sandwich!")

        finished_sandwiches.append(order)
        sandwich_orders.remove(order)
        break
    
print("\nSandwiches that i made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()} sandwich")
