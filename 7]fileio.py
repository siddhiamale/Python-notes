''' FILE I/O 
       Python can be used to perform operations on a file.(read & write data)
       
    Types of file :-
    1.Text Files : .txt,.docx,.log etc
    2.Binary Files : .mp4,.mov,.png,.jpeg etc  
    
    
    Open, read & close file
       We have to open a file before reading or writing.
       f = open("file_name","mode")      ----mode = r:read mode,w:write mode
                                         ----file_name = sample.txt,demo.docx
    
      data = f.read()       ---reads entire file
      data = f.readline()   ---reads one line at a time
      f.close()
       
       '''

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

''' MODES
    'r'  => open for reading(default)
    'w'  => open for writing.content is overwritten.
    'x'  => create a new file and open it for writing
    'a'  => open for writing,appending to the end of file if it exists.
    'b'  => binary mode
    't'  => text mode(default)
    '+'  => open a disk file for updating(reading and writing)
    'r+' => read+overwrite(pointer at start)-no truncate
    'w+' => read+overwrite-truncate
    'a+' => read+append(pointer at end)-no truncate
'''

# Writing to a file
f = open("demo.txt","w")
f.write("this is a new line")               # overwrites the entire file

f = open("demo.txt","a")
f.write("this is a new line")               # adds to the file

# With syntax :-
with open("demo.txt","a") as f:                        # automatically closes the file.
    data = f.read()                
 

''' Deleting a file 
    using the os module
    Module(like a code library) is a file written by another programmer 
      that generally has a function we can use.
      '''
import os
os.remove("sample.txt")