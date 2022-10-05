n=int(input("how many term "))
x1=0
x2=1
count=0
if n<=1:
    print(x1)
elif n<=2:
    print(x1,x2,end=" ")
else:
    print("fibconaci series ")
    while count <n :
      print(x1)
      x1=x2
      nth=x1+x2
      x2=nth
      count+=1



    

