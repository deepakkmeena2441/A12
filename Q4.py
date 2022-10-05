# to print prime number between two given number both are inclusive
def prime(n1,n2):
    i=2
    for e in range(n1,n2+1):
        for d in range(2,e):
            if e%d==0:
                break
            
        else :
            print(e)






prime(int(input()),int(input()))