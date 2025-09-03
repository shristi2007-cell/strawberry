x=('a','b','c')
print(type(x))

#always small bracket for tuple


#changing tuple to list and viceversa:
lst=list(x)
print(lst)     

tup=tuple(lst)
print(tup)

x,y,z=(1,2,3)
print(x)
print(y)
print(z)

#if you want to assign more values to z :
x,y,*z=(1,2,3,4,5)
print(x)
print(y)
print(z)

*x,y,z=(1,2,3,4,5)
print(x)
