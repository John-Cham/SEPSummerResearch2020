a = [1,2,3,4,5,6]
b = [3,4,'na',6,7,8]
c= [5,6,7,8,9,10]

abc= list(zip(a,b,c))
length_abc= len(abc[0])

def division(value):
    return(value/length_abc)

sum_abc= map(sum,abc)

mean = map(division, sum_abc)
print(list(mean))

