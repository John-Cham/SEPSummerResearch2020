import os

os.chdir('/Users/John/Downloads/')

meth_dict= {}

with open('test_file.txt', 'r') as reader: 
    for line in reader:
      if line.startswith('Hugo_Symbol'):
         header = line
      else:
         meth_data= line.strip().split('\t')    
         hugo_symbol= meth_data[0]
         meth_data.pop(0)

         if hugo_symbol not in meth_dict:
            meth_dict[hugo_symbol] = [meth_data]
         else:
            meth_dict[hugo_symbol].append(meth_data)
            
for key in meth_dict:
    meth_dict[key] = [list(map(float, sublist)) for sublist in meth_dict[key]]
    if len(meth_dict[key])>1:
        tcga= list(zip(*meth_dict[key]))
        length_tcga= len(tcga[0])
        def division(value):
            return(value/length_tcga)
        sum_tcga= map(sum,tcga)
        mean = map(division, sum_tcga)
        meth_dict[key]= (list(mean))
print(meth_dict)