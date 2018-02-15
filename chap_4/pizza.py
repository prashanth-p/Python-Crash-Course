pizzas = ["margarita", "tomato", "onion", "paneer", "corn", "olives"]
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really love pizzas")

friend_pizzas = ["farmhouse", "overloaded", "paporoni"]
for pizza in friend_pizzas:
    print("My friend likes " + pizza + " pizza")

print(pizzas == friend_pizzas)

print("the first three pizzas I love are: ", pizzas[0:3])
print("from middle to end: ", pizzas[round(len(pizzas) / 2):])
print("Last three items in the list ", pizzas[-3:])
