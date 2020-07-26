import os

os.chdir('/Users/John/Downloads/')

def List_Maker(string): 
    li = list(string.split("\t"))
    return li

#never mind i figure out how to print the Hugo symbols
with open('test_file.txt', 'r') as reader:
    x= List_Maker(reader.readline())
    for i in x: 
            x= List_Maker(reader.readline())   
            print(x[0])
        