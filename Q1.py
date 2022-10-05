n=int(input("enter the number"))
number=0
while n>0:
    c=n%10
    number=number*10 + c
    n=n//10
print(number) 



