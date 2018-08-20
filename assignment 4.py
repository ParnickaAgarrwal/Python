#LIST AND STRINGS METHODS

#Q.1- Reverse the whole list using list methods.
list=[0,10,20,30,40,50]
print(list[::-1])


#Q.2- Print all the uppercase letters from a string.
string=input("Enter the string ")
for i in range(0,len(string)):
    if (string[i]>='A' and string[i]<='Z'):
        print("The uppercase letter in the string : ",string[i])


#Q.3-Split the user input on comma's and store the values in a list as integers.
number=int(input("Enter number of values "))
list1=[int(input("Enter the values ")) for i in range(number)]
print(list1)


#Q.4- Check whether a string is palindromic or not.
string1=input("Enter a string: ")
if(string1==string1[::-1]):
      print(string1," is a palindrome.")
else:
      print(string1," isn't a palindrome.")


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
print("A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.")
import copy as c
list_1=[1,2,[3,4],5]
print("List 1 is ",list_1)
list_2=c.copy(lis_1)
print("List 2 is ", list_2)
list_1[2][0]='Done'
print("Now list 2 is ",list2_,"\nand list 1 is ",list1_)
list_1[1]='Changed'
print("List 1 is ",list_1)
print("List 2 is ", list_2)
print("A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.")
list_a=[1,2,3,4]
print("List a is ",list_a)
list_b=list_a
print("List b is ", list_b)
list_b[0]='Hey'
print("Now list b is ",list_b, "\n and a is ",list_a)

