# WAP to check given number is armstrong or not

n=int(input("enter number:"))
temp=n
sum=0
while n>0:
    dig=n%10
    sum=sum+(dig**3)
    n=n//10
if(temp==sum):
    print("number is armstrong") 
else:
    print("number is not armstrong")       