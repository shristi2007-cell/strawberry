#question1: get the sum of all values inside matrix
#fruits=['kiwi','cherry','pine,'banana','apple','Orange']

#question2: arrange the above fruits list in ascending order called new_fruits
#question3: make all the letters in word capital and create new list using list comprehension


#2
fruits= ['kiwi','cherry','pine','banana','apple','Orange']
fruits.sort()
print(fruits)

#3

new_fruits=[fruit.upper() for fruit in fruits]
print(new_fruits)

new_fruit=[fruit.lower() for fruit in fruits]
print(new_fruit)

         


