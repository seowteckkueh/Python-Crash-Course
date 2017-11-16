pizzas=['pepperoni pizza','cheeze pizza','hawaiian supreme pizza']
for pizza in pizzas:
	print("I like "+pizza.title()+"!\n")
print("I really love pizza!\n")

friend_pizzas=pizzas[:]
pizzas.append('thai pizza')
friend_pizzas.append('spicy kimchi pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\n")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
