#Exceptional case for zero error:
try:
    x=int(input('enter a number:'))
    y=int(input('enter second number:'))
    result=x/y
    print(result)

except ZeroDivisionError as e:
    print(e)
    print('you have entered zero.')
    x=int(input('enter first number:'))
    y=int(input('enter second number:'))
    result=x/y
    print('result:',result)

except ValueError as e:
    print(e)
    print('you have entered zero.')
    x=int(input('enter first number:'))
    y=int(input('enter second number:'))
    result=x/y
    print('result:',result)


#alt
#def divide():
try:
    x=int(input('enter the number for x:'))
    y=int(input('enter the number for y:'))
    result=x/y
    print('result:',result)

except Exception as e:
    print(f'error:{e}')
    x=int(input('enter the number for x:'))
    y=int(input('enter the number for y:'))
    result=x/y
    print('result:',result)
