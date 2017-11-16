foods=['pizza','burger','spaghetti','chips','sandwich','coke']
print("The first three items in the list are:")
for food in foods[:3]:
	print(food.title())
print("\n")

print("Three items from the middle of the list are:")
for food in foods[1:4]:
	print(food.title())
print("\n")

print("The last three items in the list are:")
for food in foods[-3:]:
		print(food.title())
