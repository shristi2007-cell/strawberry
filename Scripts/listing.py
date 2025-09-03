num=[1,2,3,4]
fruits=['apple','banana','cherry']
mixed_list=[10,'hello',True,3.14]

print(num[1:])
print(fruits[0:2])
print(mixed_list[2:])

fruits[0]='orange'
print(fruits)
fruits.append('strawberry')        #adding elements
print(fruits)
fruits.remove('banana')            #removing elemnts
print(fruits)
fruits.insert(2,'dragon')         #inserting in between 
print(fruits)

for fruit in fruits:              #prints single fruit
    print(fruit)

index=0
while index< len(fruits):
    print(fruits[index])
    index+=1