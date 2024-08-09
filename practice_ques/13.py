# WAP to find Fibonacci of a number

n=10
n1,n2=(0,1)
temp=n2
i=1
while i<=n:
    print(temp,end=" ")
    i += 1
    n1,n2=n2,temp
    temp=n1+n2
    