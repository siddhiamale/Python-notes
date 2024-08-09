# WAP to find maximum of three numbers

def maxof3(a,b,c):
    if (a > b and a > c):
        print(a,"is maximum")
    elif (b > a and b > c):
        print(b,"is maximum")
    else:
        print(c,"is maximum")

maxof3(4,9,7)