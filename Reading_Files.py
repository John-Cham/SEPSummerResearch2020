import os

os.chdir('/Users/John/Downloads/')

def List_Maker(string): 
    li = list(string.split("\t"))
    return li 

#I tried to make this a for loop but it would only out put every other hugo symbol 
with open('test_file.txt', 'r') as reader:
#   for line in reader:   
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])
    
    x= List_Maker(reader.readline())
    print(x[0])