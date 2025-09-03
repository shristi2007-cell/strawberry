#another method:
numbers=[1,2,3,3,3,4,5,6,7,8,9]
output=[]
for number in numbers:
    if(number not in output):
        output.append(number)
print(output)