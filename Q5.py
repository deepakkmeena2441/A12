def prime(n):
    
    while True:
     n+=1
     i=2
     while i<n:
        if n%i==0:
            break
        i+=1
     else:
        return n
    
    
n=int(input())
c=prime(n)
print("next prime number of given number is ",c)
