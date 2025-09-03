class Person :
    def __init__(self,name,age):
        self.name=name 
        self.age=age

    def greet (self):
        return f'hello, my name is {self.name} and i am {self.age}yearas old'
    
#creating instances(objects of the person)
person1=Person('alice',30)
person2=Person('bob',30)


print(person1.name, person1.age)






print(person2.name, person2.age)

#Heritance:
class animal:
    def speak(self,name):
        return f'Animals speak'
    
animal1=animal('dog','bark')
animal2=animal('tiger','roar')

print(animal1.name,animal.speak)
print(animal2.name,animal.speak)

    
        