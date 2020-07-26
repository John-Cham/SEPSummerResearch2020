import os

os.chdir('/Users/John/Downloads/')

def List_Maker(string): 
    li = list(string.split("\t"))
    return li


with open('test_file.txt', 'r') as reader:
    x= List_Maker(reader.readline())
    for i in x: 
            x= List_Maker(reader.readline())   
            Hugo_symbol= [x[0]]
            x.pop(0)
            TCGA = x
            Hugo_dict= dict(zip(Hugo_symbol, TCGA))
            print(Hugo_dict)   
#gonna work some more on this tomorrow I know that this is incorrect. I cannot seem to access the values using the keys. It should just be one dictionary but the for loop makes it multiple


#fruits = ["Apple", "Pear", "Peach", "Banana"]
#prices = [0.35, 0.40, 0.40, 0.28]

#fruit_dictionary = dict(zip(fruits, prices))

#print(fruit_dictionary)
#Remove the first element (Hugo Symbol) from the arrayadd the Hugo symbol as the key
#and the new list as the value.

#maybe I make two lists make these outputs a list and make the dictionary of values a seperate list 