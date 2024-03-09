#create a list called menu
cafe_menu = ["Espresso", "Cappuccino", "Mocha", "Latte", "Americano", "Hot Chocolate"]

#create a dictionary called 'stock' containing the stock value for each item on the menu
stock = {
  "Espresso": 20,
  "Cappuccino": 15,
  "Mocha": 10,
  "Latte": 10,
  "Americano": 30,
  "Hot Chocolate": 8
}

# Create a dictionary called price, containing the prices for each item on the menu
price = {
  "Espresso": 3.00,
  "Cappuccino": 4.05,
  "Mocha": 4.15,
  "Latte": 4.05,
  "Americano": 3.60,
  "Hot Chocolate": 4.15
}

# calculate the total stock worth by looping through the dictionaries and list
total_stock = 0
for items in stock:
  total_stock += stock[items] * price[items]

# print the total stock worth
print(f"The total stock worth is: £{total_stock}\n")

# print the menu with prices
print("Menu: \n")
for items in cafe_menu:
  print(f"{items} - £{price[items]}")

# print the stock availability
print("\nStock Availability: \n")
for items in stock:
  print(items, "-", stock[items])
