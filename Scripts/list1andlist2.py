#list1 and list2

lst1=[1,2,3,4,5]
lst2= lst1
print('lst1',lst1)
print('lst2=',lst2)

#if I update in lst2:
lst2.append(6)
print(lst2)
print(lst1)          #lst1 also gets updated

#if i want to update lst2 only:
lst2=lst1.copy()
lst2.append(7)
print(lst2)
print(lst1)         #lst1 doesnt get updated


#List comprehension


#normal method:
fruits=['apple','banana','cherry']
new_fruits=[]
for fruit in fruits:
    if 'a' in fruit:
        print(fruit)
        new_fruits.append(fruit)
        print('new fruit:',new_fruits)

#list comprehension method:
new_fruits=[fruit for fruit in fruits if 'a' in fruit]
print('newfruits:',new_fruits)

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

list=[1,2,3,4,5,6,7]
new_list=[x**2 for x in numbers]
   



    
