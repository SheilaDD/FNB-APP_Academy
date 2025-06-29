

foods= []  # Initialize an empty list for food itemsp
prices = []
total = 0

while True:
    food = input("Enter a food item or q once done: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
        foods.append(food)
        prices.append(price)
      
print("________your shopping cart________")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Total price: R{total}")