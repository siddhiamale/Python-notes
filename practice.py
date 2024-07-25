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
# PART 3
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
copy_list = list.copy()
copy_list.reverse()
if (list == copy_list):
    print("list is palindrome")
else:
    print("list is not palindrome")    
    

# WAP to count the number of students with the "A" grade.
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


# Store above values in a list & sort them from "A" to "D".
grade = ["C","D","A","A","B","B","A"]
print(grade.sort())


#-------------------------------------------------------------------------------------------------------------------------------------------------------
# PART 4
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Store the following word meaning in python dictionary:
#     table : "a piece of furniture","list of facts and figures"
#     cat : "a small animal"
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts and figures"]
}

print(dict)


''' You are given list of subjects for students.Assume one classroom is required for one subject.
      How many classrooms are needed by all students
        python,java,C++,python,javascript,java,python,java,C++,C
       
'''
class_list = {"python","java","C++","python","javascript","java","python","java","C++","C"}

print(len(class_list))     # 5


#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PART 5
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1


# Print numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1


# Print multiplication table for a number n
n = int(input("ENter no:-"))
i = 1
while i <= 10:
    print(f"{n} * {i} = {n*i}")
    i += 1


# Print the elements of the following list using python
# [1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# Search for number x in this tuple using loop
#  (1,4,9,16,25,36,49,64,81,100)
x = 64
nums = (1,4,9,16,25,36,49,64,81,100)
idx = 0
while idx <= len(nums):
    if(nums[idx] == x):
        print("no found at index",idx)
    idx += 1


# using for and range
# Print numbers from 1 to 100
for i in range(1,101):
    print(i)


# Print numbers from 100 to 1
for i in range (100,0,-1):
    print(i)


# Print multiplication table of a number n
n = 5
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")


# WAP to find the sum of first n numbers (using while)
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum) 


# WAP to find factorial of first n numbers (using for)
n = 5
fact = 1
i = 1
for i in range(1,n+1):
    fact *= i
    i += 1
print(fact)    


#------------------------------------------------------------------------------------------------------------------------------------------------------
# PART 6
#---------------------------------------------------------------------------------------------------------------------------------------------------
# WAF to print the length of list.(list is the parameter)
cities = ["nashik","sinnar","pune","sangamner"]
nums = [2,4,7,5,4,5,4,8,7,4,3,6,9]
def length(list):
    print(len(list))

length(cities)    
length(nums)               # 4,13


# WAF to print the elements of list in a single line.(list is the parameter)
cities = ["nashik","sinnar","pune","sangamner"]
nums = [2,4,7,5,4,5,4,]
def length(list):
    for ele in list:
        print(ele,end=" ")

length(cities)
length(nums)        


# WAF to find the factorial of n.(n is the parameter)
def find_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)  

find_fact(5)      


# WAF to convert USD to INR
def convert(usd):
    total=usd*83
    print(f"{usd} USD = {total} INR")

convert(10)    


# Even Odd
def oddEven(n):
    if (n % 2 == 0):
        print(n,"is even")
    else:
        print(n,"is odd")

oddEven(33)
