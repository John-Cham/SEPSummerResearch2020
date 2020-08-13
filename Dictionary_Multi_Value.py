import os

os.chdir('/Users/John/Downloads/')

meth_dict= {}

with open('data_acc_methylation_hm27.txt', 'r') as reader: 
    for line in reader:
      if line.startswith('Hugo_Symbol'):
         header = line
      else:
         meth_data= line.strip().split('\t')    
         hugo_symbol= meth_data[1]
         meth_data.pop(1)
         if hugo_symbol not in meth_dict:
            meth_dict[hugo_symbol] = [meth_data]
         else:
            meth_dict[hugo_symbol].append(meth_data)

print(meth_dict)