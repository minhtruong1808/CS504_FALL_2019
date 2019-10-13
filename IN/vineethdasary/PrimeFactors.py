# Python program to check if the input number is prime or not


# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
       # check for factors
    count = 0
    for i in range(1, num+1):
        if (num % i) == 0:
            count=count+1
            # print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
        
    if count == 2:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
    print(num,"is not a prime number")