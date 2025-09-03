#raise custom exception to handle different cases with same except block:
x=int(input('enter your age:'))
try:

    if x>100:
        raise Exception('sorry,no numbers above 100')
    elif x==0:
        raise Exception('Sorry, age is not zero. Please enter in months:')
    print(f'my age is {x}')

except Exception as e:
    print(e)
    x=int(input('Re-enter your age:'))
    print(f'my age is {x}')
