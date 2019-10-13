# message prompt
print('This program will sum the numbers from 1 to a number you enter.')
print('Please enter an ending number')

# ask user input
num: int = int(input())
total: int = 0   # initialize variable

while num >= 1:
  total += num    # accumulator
  num -= 1        # decrement

# print output
print('The sum is: ' + str(total))
