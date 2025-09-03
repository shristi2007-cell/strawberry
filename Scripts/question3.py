#question3:
#numbers=[1,2,3,3,3,4,5,6,7,8,9]
#create new list with only unique value from above list numbers.

numbers=[1,2,3,3,3,4,5,6,7,8,9]
for number in numbers:
    counter= numbers.count(number)
    if counter>=2:
        for x in range(counter-1):
            numbers.remove(number)
            print(numbers)


#another method:
numbers=[1,2,3,3,3,4,5,6,7,8,9]
output=[]
for number in numbers:
    if(number not in output):
        output.append(number)
print(output)





   