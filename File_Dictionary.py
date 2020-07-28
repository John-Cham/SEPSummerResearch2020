import os

os.chdir('/Users/John/Downloads/')



meth_dict= {}
with open('test_file.txt', 'r') as reader:
    next(reader) 
    for line in reader:
        meth_data= line.strip().split('\t')    
        hugo_symbol= meth_data[0]
        meth_data.pop(0)
        meth_dict[hugo_symbol]=meth_data
print (meth_dict)
           

