def Fibonacci(n):
    a=0
    b=1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    return c


x=Fibonacci(1000)
print(x)