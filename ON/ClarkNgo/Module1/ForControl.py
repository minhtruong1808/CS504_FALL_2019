# use library random to access random API
import random

# loop 1 to 5 ~ 15 times using random API
for i in range(1, random.randint(5, 15)):
  # convert int variable i to string
  print('This for loop has already run ' + str(i) + ' times.')
