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


#Q.4- create a list with numbers and sort it in ascending order.
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


#Q.6-Implement a stack and queue using lists.
stack=["abc","def","ghi","jkl"]
print("Stack is: ",stack)
stack.append("mno")
print("Updated stack is: ",stack)
stack.append("pqr")
print("Updated stack is: ",stack)
print("Popped value: ",stack.pop())
print("Updated stack is: ",stack)
queue=[0,1,2,3,4,5,6,7,8,9]
print("Queue is: ",queue)
queue.append(10)
print("Updated queue is: ",queue)
queue.pop(0)
print("Updated queue is: ",queue)


'''OPTIONAL QUESTION
Q.1- Count even and odd numbers in that list.'''
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
