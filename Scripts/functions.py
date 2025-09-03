def add(a,b):
    result=a+b
    print(result)
add(18,18)
add(20,1)

#alternative:
def add():
    a=10
    b=20
    result=a+b
    print(result)
add()

#alternative:
def add(a,b):
    result=a+b
    print(result)

x=20
y=0
add(x,y)

#parameter less and with return type:
def add():
    a=10
    b=20
    result=a+b
    return result
final_value =add()
print(final_value)


#with parameter and with return type:
def add(a,b):
    result=a+b
    return result
final_result=add(10,20)
print(final_result)

#function using list:

def calculate(numbers):
    min_value =min(numbers)
    max_value= max(numbers)
    sum_value=sum(numbers)
    return min_value, max_value ,sum_value

numbers=[1,2,3,4,5]       #(function call)
min_value, max_value, sum_value = calculate(numbers)

print('minimum:' ,min_value)
print('maximum:',max_value)
print('sum:',sum_value)


#default case:
def calculate(a,b):
    result1=a+b
    resul2=a-b
    return result1
final=calculate(10,20)
print(final)

#for default:
def calculate(a,b=0):
    result1=a+b
    resul2=a-b
    return result1
final=calculate(10)
print(final)

#default should always be in right side if you want to default a then calculate(b,a=0)


#arguments:
def calculate(*args): #for tuples
    print(args)
calculate(10,20,30,40)

def calculate(**kwargs):
    print(kwargs)
calculate(a=10,b=20,c=30,d=40)

def calculatee(*args,**kwargs):
    print(args,kwargs)
calculatee(1,2,3,4,5,a=10,b=20,c=40)