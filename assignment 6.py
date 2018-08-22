#FUNCTIONS
#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def areaofsphere(radius):
    return 4*3.14*(radius**2)
radius = int(input("Enter the radius of sphere: "))
print(areaofsphere(radius))


'''Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].'''
def perfectNumber(n):
    list=[]
    for i in range(1,n):
        if(n%i==0):
            list.append(i)
    if(sum(list)==n):
        return True
for i in range(1,1001):
    if(perfectNumber(i)):
        print(i,"is a perfect number")


#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
def printmultiplicationtable(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
n = int(input("Enter the number: "))
printmultiplicationtable(n)


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power(base,exponent):
    if(exponent==1):
        return(base)
    if(exponent!=1):
        return(base*power(base,exponent-1))
base=int(input("Enter base: "))
exponent=int(input("Enter exponent: "))
print("Answer is:",power(base,exponent))

