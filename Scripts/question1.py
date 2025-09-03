#question:
#fruits=['apple','banana','orange','cherry','grapes','kiwi']
#create the new list from above lists by taking all the elements in fruits list that have an 'a' in it

fruits=['apple','banana','orange','cherry','grapes','kiwi']
for fruit in fruits:
    if 'a' in fruit :
        print(fruit)


#question2:
#numbers=[1,2,3,4,5,6,7,8,9]
#create new list by taking only odd value from above number list

numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number%2!=0:
        print(number)
