numbers=[8,9,9,3,4,5,6]
numbers.sort(reverse=True)
print(numbers)


#sorting: it sorts alphabetically
animals=['cow','monkey','zebra', 'ant', 'duck']
animals.sort()
print(animals)

#sorting reverse: sorts from last letters
animals.sort(reverse=True)
print(animals)

#If capital letters are present it comes first 
animals=['Cow','monkey','zebra', 'ant', 'duck']
animals.sort()
print(animals)

#SORTED:
numbers=[4,3,5,6,8]
sorted_numbers=sorted(numbers)
print(sorted_numbers)              #it sortes numbers 
print(numbers)                     #prints original numbers

sorted_numbers=sorted(numbers (reverse=True))
print(sorted_numbers)