toppings = ["pepperoni", "pineapple", "cheese", "sausage" "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print("We sell {} different kinds of pizza!".format(num_pizzas))

pizza_and_prices = [["pepperoni", 2], ["pineapple", 6], ["cheese", 1], ["sausage", 3], ["olives", 2], ["anchovies", 7], ["mushrooms", 2]]
print(pizza_and_prices)

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()
pizza_and_prices.insert(1, ["peppers", 2.5])
pizza_and_prices.sort()

three_cheapest = pizza_and_prices[-3:]
print(three_cheapest)