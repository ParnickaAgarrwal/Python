'''#DECISION AND FLOW CONTROL
#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter the year: "))
if(year%4==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("Enter the length: "))
breadth=int(input("Enter the breadth: "))
if(length==breadth):
    print("These are dimensions of square.")
else:
    print("These are dimensions of rectangle.")


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("Enter the age of first person: "))
b=int(input("Enter the age of second person: "))
c=int(input("Enter the age of third person: "))
if(a>b and a>c):
    print(a,"is the oldest.")
elif(b>a and b>c):
    print(b," is the oldest.")
elif(c>a and c>b):
    print(c,"is the oldest.")
    if(a<b and a<c):
        print(a,"is the youngest.")
    elif(b<a and b<c):
        print(b,"is the youngest.")
    else:
        print(c,"is the youngest.")


'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR".'''
age=int(input("Enter the age: "))
sex=input("Enter either M or F: ")
maritalstatus=input("Enter either Y or N: ")
if(sex=='F'):
    print("Will work only in urban areas.")
elif(sex=='M'):
    if(age>=20 and age<40):
        print("Can work anywhere.")
    elif(age>=40 and age<60):
        print("Will work in urban areas only.")
    else:
        print("ERROR")


#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("Enter the quantity: "))
if((quantity*100)> 1000):
    print("Cost is: ",((quantity*100)-(.1*quantity*100)))
else:
    print("Cost is: ",quantity*100)


#LOOPS
'''Let’s iterate your minds with loops.. 
Q.1- Take 10 integers from user and print it on screen.'''
l=[]
for i in range(0, 10):
        num=int(input("Enter number: "))
        l.append(num)
print("Numbers entered by the user are:",l)


#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while(1>0):
    print("An infinte loop never ends. Condition is always true.")


#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
list=[]
square=[]
for i in range(0,5):
    n=int(input("Enter the number: "))
    list.append(n)
print("The original elements entered are:",list)
for i in list:
    square.append(i ** 2)
print("The squared list is:",square)


#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
li=[ 4,'a', 'b', 'c', 1, 'd', 3.1]
integers=[]
strings=[]
floats=[]
for i in li:
    if(isinstance(i,str)):
        strings.append(i)
    elif(isinstance(i,int)):
        integers.append(i)
    elif(isinstance(i,float)):
        floats.append(i)
print("Strings are:",strings)
print("Integers are:",integers)
print("Floats are:",floats)


#Q.5- Using range(1,101), make a list containing only prime numbers.
prime=[]
for i in range(1,101):
    c=0
    for j in range(2,i):
        if(i%j==0):
            c=1
            break;
    if(c==0):
            prime.append(i)
print(prime)
'''

'''Q.6- Print the following patterns: 
* 
** 
*** 
****'''
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")


#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.  
lis = [2,1,3,5,4,8]
print("Initial list is:",lis)
n=int(input("Enter number to be deleted: "))
if n in lis:
    lis.remove(n)
    print("List after deleting the element is:",lis)
else:
    print("Entered number is not present in the list.")

        
