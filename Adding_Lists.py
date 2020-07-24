a = [1,2,3,4,5,6]
b = [3,4,5,6,7,8]
c= [5,6,7,8,9,10]

x= zip(a,b,c)
n= 3
#I should find a way to have n be calculated instead of me knowing it is 3
# len(x) doesnt work


y= map(sum,x)

for i in y:
    mean= (i/n)
    print(mean)