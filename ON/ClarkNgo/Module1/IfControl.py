# message prompt
print('How old are you?')

# add type safe int
# ask user input
age: int = int(input())

# conditional statement block
if age < 22:
  print('You are too young to have a drink.')
elif age >= 80:
  print('Ok, you will get a free drink.')
else:
  print('Sure, enjoy your drink.')
