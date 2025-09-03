
#Empty dictionary
empty_dict={}

#Dictionary with initial values
my_dict={
    'name': 'alice',
    'age' : 30,
    'city': 'new york'
}
print(my_dict)

#mixed dictionary 
mixed_dict={
    1: 'one',
    2: 'two',
    (1, 2): 'tuple'
}
print(mixed_dict)

print(my_dict['city'])
print(my_dict.get('address',1))
print(my_dict)

#for updating values:
my_dict['age']=31    
print(my_dict)

#for adding new key value:
my_dict['gender']='female'
print(my_dict)

del my_dict['city']     #remove a specific key value pair
my_dict.pop('age')      #remove a specific value associated with it
print(my_dict)          

for x in my_dict:
    print(my_dict[x])

for x in my_dict.keys():
    print(x)

for x in my_dict.values():
    print(x)

for k,v in my_dict.items():   #gives both keys and values
    print(k)
    print(v)

#note: my_dict[x]:only prints key , my_dict.keys(): prints only keys , my_dict.values():prints only values, my_dict.items(): prints both 

my_dict.clear()
print(my_dict)

