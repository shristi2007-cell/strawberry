
#List comprehension


#normal method:
fruits=['apple','banana','cherry']
new_fruits=[]
for fruit in fruits:
    if 'a' in fruit:
        print(fruit)
        new_fruits.append(fruit)
        print('new fruit:',new_fruits)

new_fruits=[fruit for fruit in fruits if 'a' in fruit]
print('newfruits:',new_fruits)

#normal method:
numbers=[1,2,3,4,5]
new_numbers=[]
for number in numbers:
    if number%2==0:
        new_numbers.append('even')
    else:
        new_numbers.append('odd')
    print(new_numbers)

    
#using list comprension:
new_numbers=['even' if number%2==0 else 'odd' for x in numbers]

list=[1,2,3,4,5,6]
new_list=[x**2 for x in list]
   


