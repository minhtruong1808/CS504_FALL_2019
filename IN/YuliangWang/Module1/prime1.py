#python program to check the prime number 
#creating a array load the prime number
l = []
#take input from the user
for x in range(int (input("please enter a number:"))):
   #when the range less than 2
   if x <2:
      continue
   #check for factors
   for i in range(2,x):
      if x%i ==0:
         break
   #record the prime number
   else:
      l.append(x)
#output the array
print(l)