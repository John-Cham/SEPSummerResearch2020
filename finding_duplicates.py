import os

os.chdir('/Users/John/Downloads/')

hugo_symbol= []
with open('data_acc_methylation_hm27.txt', 'r') as reader:
    next(reader) 
    for line in reader:
        meth_data= line.strip().split('\t')    
        hugo_symbol.append(meth_data[1])

duplicates = []
unique = {}
for x in hugo_symbol:
   if x not in unique:
      unique[x] = 1
   else:
      if unique[x] == 1:
         duplicates.append(x)
      unique[x] += 1
print(duplicates)
 
