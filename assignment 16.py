#MONGODB WITH PYTHON
#Q.1- Write a python script to create a databse of students named Students.
import pymongo
client=pymongo.MongoClient()
data=client['Students']
collection=data['student']

'''Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
AND
Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.'''
'''for i in range(10):
    name = input('Enter name: ')
    marks = int(input('Enter marks: '))
    collection.insert_one({'name':xyz,'marks':90})
d =collection.find()
for doc in d:
    print(doc)'''
i=0
while(i<10):
    try:
        name = input("Enter the name: ")     
        marks = int(input('Enter your marks: '))
        if(marks<0 or marks >100):               
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:
            collection.insert_one({'name':name,'marks':marks}) 
            i=i+1
    except  ValueError as msg:
        print(msg)


#Q.4- Print the names of all the students who scored more than 80 marks.
print("Name of students with marks more than 80:")
p=collection.find({'marks':{'$gt':80}})
for i in p:
    print(i)
