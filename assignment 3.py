#LIST
#Q.1- Create a list with user defined inputs.
list=[]
n=int(input("Enter how much integers you want in the list\n"))
print("Enter the elements")
for i in range(n):
    a=int(input())
    list.append(a)
print(list)


'''Q.2- Add the following list to above created list:
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]'''
list1=['google','apple','facebook','microsoft','tesla']
list.extend(list1)
print(list)


#Q.3- Count the number of time an object occurs in a list.
l=[1,2,3,4,5,6,7,8,9,1,1,1,2,]
print(l.count(1))


#Q.4- Create a list with numbers and sort it in ascending order.
l1=[1,0,56,25,79,589,24792,2548]
l1.sort()
print(l1)


'''Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]'''
A=[1,0,58,2561,22]
print("A is:",A)
B=[3,2,5,1597,289]
print("B is:",B)
A.sort()
B.sort()
print("Sorted A is:",A)
print("Sorted B is:",B)
A.extend(B)
print("Merged is:",A)
A.sort()
print("Sorted merged list is:",A)


#Q.6-Count even and odd numbers in that list.'''
num=[23,24,18,7,3,8]
countodd=0
counteven=0
for i in num:
    if(i%2==0):
        counteven+=1
    else:
        countodd+=1
print("The list is: ",num)
print("The odd count is: " , countodd)
print("The even count is: ",counteven)


#TUPLES
#Q.1-Print a tuple in reverse order.
tuple=(1,2,3)
print("The tuple is:",tuple)
print("The reversed tuple is:" ,tuple[::-1])


#Q.2-Find largest and smallest elements of a tuples. 
tuple1=(1,0,5,7896,659,-1879)
print("The maximum element is:",max(tuple1))
print("The minimum element is:",min(tuple1))

#STRINGS
#Q.1- Convert a string to uppercase.
string="Hello Acadview"
print(string.upper())


#Q.2- Print true if the string contains all numeric characters.
string1=str(input("Enter a string "))
print(string1.isdigit())


#Q.3- Replace the word "World" with your name in the string "Hello World".
string2="Hello World"
print(string2.replace('World','Parnicka Agarrwal'))
