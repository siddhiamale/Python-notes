# WAP to find minimum of three numbers

def minof3(a,b,c):
    if (a < b and a < c):
        print(a,"is minimum")
    elif (b < a and b < c):
        print(b,"is minimum")
    else:
        print(c,"is minimum")

minof3(4,9,7)