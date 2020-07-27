import os

os.chdir('/Users/John/Downloads/')


with open('test_file.txt', 'r') as reader:
    next(reader)
    #I did this because I was unable to take notes on how you were able to skip the first line
    for line in reader:
        meth_data= line.strip().split('\t')
        print(meth_data[0])
        
    
