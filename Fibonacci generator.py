def fibo(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(num):
        c=a+b
        yield c
        a=b
        b=c
for x in fibo(num=int(input("Enter a number to find fibonacci Series:"))):
    print(x)