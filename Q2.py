def prime(n):
    i=2
    while i<n:
        if n%i==0:
            break
        i+=1
    else:
        print("number is prime ",n)
         



n=int(input())
prime(n)


