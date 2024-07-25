# FUNCTION :- Block of statement that perform a specific task.
''' syntax :-   def function_name(para1,para2):     ----function definition
                      #some work
                      # return val   
                       
                function_name(para1,para2)        ----function call   '''

# e.g =>

def sum(a,b):
    s=a+b
    return s

sum(5,9)

# ****************************************************************************************************************************************
''' Built in functions :- the functions that are already defined by python itself
     print()
     len()
     type()
     range()
     
    User-defined functions :- the functions that are created and used by programmer  ''' 

# ******************************************************************************************************************************************

# Default Parameter :- Assigning a default value to parameter ,which is used when no argument is passed.
def cal_prod(a=3,b=3):
    return a*b

cal_prod()

# ***********************************************************************************************************************************************
# Recursion :- When a function calls itself repeatedly.
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)                # 5 4 3 2 1

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("END")

show(3)                # 3 2 1 END END END
