# PART 1
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# WAP to input two numbers and print thier sum
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum = num1 + num2
print("The sum is",sum)                           


# WAP to input side of square & print it's area
side = float(input("Enter side:"))
area = side * side
print("Area of square is",area)


# WAP to input 2 floating point numbers & print thier average
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
avg = (num1 + num2)/2
print("Average is ",avg)


# WAP to input 2 int numbers,a and b. Print True if a is greater than or equal to b. If not print False.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if(a >= b):
    print("True")
else:
    print("False")    


#---------------------------------------------------------------------------------------------------------------------------------------------------
# PART 2
#----------------------------------------------------------------------------------------------------------------------------------------------------

# WAP to input users first name & print it's length
firstName = input("Enter your first name:")
print(len(firstName))


# WAP to find the occurences of '$' in a string
str = "hello$ world$$$....$"
print(str.count("$")) 


# WAP to grade students based on their marks
marks = int(input("enter your marks:"))

if(marks >= 90):
   print("A")
elif(marks < 90 and marks >= 80):
   print("B")
elif(marks < 80 and marks >= 70):
   print("C")
elif(marks < 70 and marks >=50):
   print("D")
else:
   print("Fail")   


# WAP to check if number entered by user is odd or even
num = int(input("Enter number:"))

if(num % 2 == 0):
   print("number is even...")
else:
   print("number is odd...")


# WAP to find the greatest of 3 numbers entered by user
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))            

if(num1 > num2 and num1 > num3):
   print(num1,"is greater...")
elif(num2 > num1 and num2 > num3):
   print(num2,"is greater...")
else:
   print(num3,"is greater")


# WAP to check if a number is multiple of 7 or not
num = int(input("enter number"))

if(num % 7 == 0):
   print(num,"is multiple of 7")
else:
   print(num,"is not multiple of 7")


#------------------------------------------------------------------------------------------------------------------------------------------------------      
# PART 2
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# WAP to ask the user to enter names of thier 3 favourite movies & store them in a list
movies = []
m1 = input("enter 1st movie:")
m2 = input("enter 2ns movie:")
m3 = input("enter 3rd movie:")

movies.append(m1)
movies.append(m2)
movies.append(m3)

print(movies)


# WAP to check if a list contains a palindrome of elements.
list = [1,2,3,2,1]
list_copy = list.copy()

if(list_copy == list.reverse()):
    print("list is palindrome..")
else:
    print("list is not palindrome..")    


# WAP to count the number of students with the "A" grade.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


# Store above values in a list & sort them from "A" to "D".
grade = ["C","D","A","A","B","B","A"]
print(grade.sort())


#-------------------------------------------------------------------------------------------------------------------------------------------------------

