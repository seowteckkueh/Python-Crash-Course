sandwich_orders = ['blt','pastrami','steak','pastrami','pastrami',
'meatball','seafood','steak']
print("Our deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
