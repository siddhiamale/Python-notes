# WHAT IS PYTHON...
''' 1)Python is simple and easy.
    2)Free and open source.
    3)High level language.
    4)Developed by Guido van Rossum.
    5)Portable  '''

#-------------------------------------------------------------------------------------------------------------------------------------------------

# First Program
#     -how print something on console or desktop

print("Helloo World...!!!")

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Variables :- A vaiable is name given to memory location in a program.

name = "Siddhi"
age = 19
SurName = "Amale"

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Data Types
''' 1) Integer  => print(type(19))          => <class 'int'>
    2) String   => print(type("siddhi))     => <class 'str'>
    3) Float    => print(type(3.141))       => <class 'float'>
    4) Boolean  => print(type(True))        => <class 'bool'>
    5) None     => print(type(complex_num)) => <class 'complex'>

'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

# Keywords => Keywords are reserved words in python.
#             Some of them are :- True,False,if,elif,else,break,contonue and so on

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Comments in Python

# This is single line comment

''' This is
     Multi-line
        comment'''

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Types of operators :- An qperator is a symbol that performs a certain operation between operands.

''' 1) Arithmetic operator (+,-,*,/,%,**,//) :- These operators are used with numeric values to perform common mathematical operations.
    2) Relational / Comparison operator (==,!=,>,<,<=,>=) :- These operators compare values
    3) Assignment operator (=,+=,-=,*=,/=,%=,**=)
    4) Logical operators (not,and,or) :- Used to combine conditional statements.
    5) Identity operator ('is'.'is not') :- Used to compare the memory locations of two objects.
        e.g=> l1 = [1,2,3]
              l2 = [1,2,3]
              l3 = l1
              print(l1 is l2)      #false
              print(l1 is l3)      #true
              print(l1 is not l3)  #false
    6) Membership operator ('in','not in') :- Used to test if a sequence is presented in an object.
        e.g=> my_list = [1,2,3,4,5]
              print(3 in my_list)     #true
              print(3 not in my_list) #false

              
    '''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Input in Python :- input() statement is used to accept values (using keyboard) from user.It returns string.

input()           #result of input() is always a str.
int(input())      #int
float(input())    #float

#----------------------------------------------------------------------------------------------------------------------------------------------------
