# WAP to find given number is prime or not

n = int(input("enter number:"))
if n>1:
    for i in range(2,(n//2)+1):
        if(n % i == 0):
            print("not a prime number")
            break
        else:
            print(n,"is prime number")
            break
else:
    print("not a prime number")        