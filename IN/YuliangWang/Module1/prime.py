# Python program to check if the input number is prime or not

# take input from the user
# num = int(input("Enter a number: "))
num = int (input('please input a number: '))
j = 0
# if input number is less than
# or equal to 1, it is not prime
if num <= 1:
   print(num,"is not a prime number")
# prime numbers are greater than 1
if num > 1:
   # check for factors
   
   for i in range(2,num):
         if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")

