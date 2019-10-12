# Python program to check if the input number is prime or not
# if it is not, show all factors

# take input from the user
num = int(input("Enter a number: "))

# define a bool variable is_prime
is_prime = True
# prime numbers are greater than 1
if num > 1:
   # check if num is not prime
   for i in range(2,num):
      if (num % i) == 0:
         is_prime = False
         print(num,"is not a prime number")
         break
   # show all the factors, otherwise show num is prime
   if is_prime == False:
      for i in range(2,num):
         if (num % i) == 0:
            print(i,"times",num//i,"is",num)
   else:
      print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
© 2019 GitHub, Inc.
