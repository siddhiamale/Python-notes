# DICTIONARY
''' Dictionaries are used to store data values in key:value pairs
    They are unordered mutable (changeable) & don't allow duplicate keys.
    We can also store list & tuple in dictionary. '''
dict = {
    "name":"siddhi",
    "age":19,
    "surname":"amale"
}
#dict["name"],dict["age"].....accessing values
#dict["key"] = "values"  .....to assign or add new value
#collection = {}         .....empty dictionary

#------------------------------------------------------------------------------------------------------------------------------------------------

# Nested dictionary

student = {
    "name" : "jay",
    "score" : {
         "maths" : 98,
         "history": 95,
         "english": 95
    }
}

print(student["score"]["maths"])   #accessing values....=>98

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Dictionary Methods
'''
    myDict.keys()               ---returns all keys
    myDict.values()             ---returns all values
    myDict.items()              ---returns all (key,val) pairs as tuples
    myDict.get("key")           ---returns key according to value
    myDict.update(newDict)      ---inserts the specified items to the dictionary

'''

#------------------------------------------------------------------------------------------------------------------------------------------------------

# SETS
''' Sets is the collection of the unordered items.
Each element in the set must be unique & immutable.
We cannot store list and dictionary in set because they are mutable. 

sets are mutable but set elements are immutable ,we can add or remove elements '''

nums = {1,2,3,4}
set_1 = {1,2,2,2}    #repeated elements are stored only once,so it will resolved to {1,2}
null_set = set()     #empty set syntax

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Set Methods

'''
   set.add(el)                ---adds an element
   set.remove(el)             ---removes an element
   set.clear()                ---empties the set
   set.pop()                  ---removes a random value
   set.union(set2)            ---combines both set values & returns new
   set.intersetion(set2)      ---combines common values & returns new
'''


#-------------------------------------------------------------------------------------------------------------------------------------------------------