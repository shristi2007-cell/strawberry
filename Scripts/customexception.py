#created custom exception to handle different cases

class negative_erroe(Exception):
    def _init_(self,message):
        supper().__init__
x=int(input('enter the age: '))
try:
    if x<0:
        raise negative_error('sorry, no numbers below zero')
    elif x==0:
        raise zero_error('sorry, age is zero')
    
except negative_error as e:
    print(e)
    print('you have entered the negative number.')
    x=int(input('re-enter your age:'))
 
except zero_error as e:
    print(e)
    print('You have entered zero as your age.Please enter your age based on months')
    x=int(input('re-enter your age:'))



    