# Strings :- String is datatype that stores sequence of characters. Strings are immutable.

# Basic operation
''' concatenation
 "helloo" + "world" => Helloworld

 length of str
 len(str)              '''

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Indexing

''' A p n a _ C o l l e  g  e
    0 1 2 3 4 5 6 7 8 9 10 11   

str="Apna_College"
str[0] is 'A'
str[1] is 'p'
str[0] = 'B'   #not allowed..  
str[-3 :-1] is 'e g'
'''

# string has negative index also starting from -1,-2...so on

#--------------------------------------------------------------------------------------------------------------------------------------------------

# Slicing :- Accessing parts of string.

'''  str[starting_idx : ending_idx]  ---enidng idx is not included
    
    str = "Apna_College"
    str[1 : 4] is "pna"
    str[ : 4] is same as str[0 : 4]
    str[1 : ] is same as str[1 : len(str)]

'''

#----------------------------------------------------------------------------------------------------------------------------------------------------

# String functions

''' str = "I am a coder."

    str.endsWith("er.")   ---returns true if string ends with substr.
    str.capitalize()      ---capitalize 1st char.
    str.replace(old,new)  ---replaces all occurences of old with new.
    str.find(word)        ---returns 1st index of 1st occurence.
    str.count("am")       ---counts the occurence of substr in string     '''

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Conditional Statements :- control statements are statements which control or change the flow of execution.

''' Syntax :-
     if (condtion):
         statement1
     elif (condition):
         statement2
     else:
         statementN        '''


#----------------------------------------------------------------------------------------------------------------------------------------------------