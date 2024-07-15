# Lists :- Abuilt-in datatype that stores set of values. It can store element of different datatypes.(int,float,str)
#           Lists are mutable.
''' marks = [87,64,33,95,74]         ---marks[0],marks[1]....
    student = ["karan",25,"delhi"]   ---student[0],student[1]....
    student[0] = "arjun"             ---allowed in python
    len(student)                     ---returns length      '''

#--------------------------------------------------------------------------------------------------------------------------------------------------

# List Slicing :- Similar to string slicing.

''' marks = [87,64,33,95,74]   
    marks[1 : 4] is [64,33,95]
    marks[ : 4] is same as marks[0 : 4]
    marks[1 : ] is same as marks[1 : len(marks)]
    marks[-3 : -1] is [33,95]
'''

#----------------------------------------------------------------------------------------------------------------------------------------------------

# List Methods 

list = [2,1,3]

list.append(4)                  #adds one element at the end [2,1,3,4]
list.sort()                     #sorts in ascending order [1,2,3]
list.sort(reverse = True)       #sorts in descending order [3,2,1]
list.reverse()                  #reverse list [3,1,2]
list.insert(1,5)                #list.insert(idx,el) --inserts element at index given [2,5,1,3]

list = [2,1,3,1]

list.remove(1)                  #removes first occuerence of element [2,3,1]
list.pop(2)                     #list.pop(idx)  --removes element at idx [2,1,1]


#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Tuples :- A built-in datatypes that let's us create immutable sequences of values.

''' tup = (87,64,33,95,74)         ---tup[0],tup[1]...
    tup[0] = 43                    ---NOT allowed in Python

    tup1 = ()
    tup2 = (1,)
    tup3 = (1,2,3)
       
'''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Tuple methods

tup = (2,1,3,1)

tup.index(1)                      #tup.index(el)  --returns index of first occurence  tup.index(1) is 1
tup.count(1)                      #tup.count(el)  --counts total occurences    tup.count(1) is 2

#-------------------------------------------------------------------------------------------------------------------------------------------------------
