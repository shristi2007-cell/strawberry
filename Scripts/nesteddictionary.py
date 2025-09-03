
#Example of a nested dictionary representing a students info

student={
    'name':'alice',
    'age':20,
    'grades':{
        'science':80, 
        'math':80,
        'english':70
    },
    'contact' : {
       'email':'alice@gmail.com',
       'phone': 9780000000
    }
}
print(student)

#question: find the sum of grades in total:

sum = 0
marks = student['grades']
for x in marks.values():
    sum = sum + x

student["total_marks"]=sum
print(student)


# #modifying nested elements:
# student['age']=21
# student['grades']['science']='86'
# student['contact']['address']='naxal'   #adding new key words
# print(student)

