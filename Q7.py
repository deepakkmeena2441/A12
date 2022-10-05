from math import gcd


n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
a=gcd(n1,n2)
if a==1:
    print("number are co-prime")
else:
    print("numbers are not co prime")