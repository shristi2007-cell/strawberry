#logging= CustomLog()

#if you want to print without order then use set:
name={'orange','banana','orange','kiwi','pine'}
#everytime it gives random output

print(name)
print(type(name))

for x in name:
    print(name)

 #adding elements:
my_set={1,2,3,4,5}
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.discard(4)
print(my_set)

num1={1,2,3,4,5}
num2={5,6,7,8,9}
num3=num1.union(num2)
print(num3)

num4=num1.intersection(num2)
print(num4)

num5={10,11}
num6=num1.union(num3,num5)
print(num6)

#for union:
num7=num1| num5
print(num7)

#for intersection:
num8=num1&num2
print(num8)

num1.intersection_update(num2)  #(num1 gets updated)
print(num1)

num2.intersection_update(num1)  #(num2 gets updated)
print(num2)

num9={1,2,3,4,5,6}
num10={2,4,6,8}
num11= num9.difference(num10)
print('num11=',num11)

#or simply use num11=num9-num10

num9.difference_update(num10)   #num9 gets updated
print(num9)

num10.symmetric_difference_update(num11)
print('num10=',num10)