#DICTIONARIES
#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
dict={}
n=int(input("Enter number of keys: "))
for i in range(0,n):
    key=input("Enter the key: ")
    value=input("Enter the value for the key: ")
    dict[key]=value
print("The dictionary is:",dict)


'''Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. 
Hint: Use nested dictionary to store subjects marks.'''
student={'Parnicka' : {}, 'information' :{}}
student['Parnicka']['Physics']=95
student['Parnicka'] ['Chemistry']=91
student['Parnicka'] ['Mathematics']=97
print(student)

