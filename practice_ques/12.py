# WAP to find factorial of a number

#using while loop
n=int(input("enter any number:"))
fact=1
i=1
while i<=n:
    fact *= i
    i += 1
print(f"factorial of given number {n} is {fact}")

#using for loop
n=5
fact=1
for i in range(1,n+1):
    fact *= i
print(f"factorial of given number {n} is {fact}")

