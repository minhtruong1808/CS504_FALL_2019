# add type safe int
price: int = 10

# prompt user
print('How many beers you want?')

# show output to user
# convert the calulated total price of price multiply by the user input to string
print('Your total price is: $' + str(price * int(input())))
