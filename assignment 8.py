'''Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.'''
class circle:
    def __init__(self):
        num=int(input("Enter the radius of the circle: "))
        self.radius=num
    def getarea(self):
        self.area=3.14*self.radius**2
        print("Area of circle is: ",self.area)
    def getCircumference(self):
        self.Circumfrence=2*3.14*self.radius
        print("Circumfrence of circle is: ",self.Circumfrence)        
s1=circle()
s1.getarea()
s1.getCircumference()


'''Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print('Name: {}, RollNo: {}, Age: {}, Marks: {}'.format(self.name, self.rollno, self.age, self.marks))
    def setAge(self,age):
        self.age=age
    def setMarks(self,mrks):
        self.marks=marks
n=input("Enter the name of the student: ")
roll=input("Enter the roll number of the student: ")
age=int(input("Enter the age: "))
marks=int(input("Enter the marks: "))
s1=Student(n,roll)
s1.setAge(age)
s1.setMarks(marks)
s1.display()


'''Q.3- Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''
class temprature:
    def convertCelsius(self,fer):
        self.fer=fer
        self.cel=((self.fer - 32)*(5/9))
        print("After conversion from farenhite to celsius: ",self.cel)
    def convertFahrenheit(self,cel):
        self.cel=cel
        self.feran=((self.cel*(9/5)) + 32)
        print("After conversion from celsius to  farenhite: ",self.feran)
fer=int(input("Enter the temprature in ferhanite: "))
celsius=int(input("Enter the temprature in celsius: "))
s1=temprature()
s1.convertFahrenheit(fer)
s1.convertCelsius(celsius)


'''Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details.'''
class MovieDetails:
    def __init__(self,artistname,year,ratings):
        self.artistname=artistname
        self.year=year
        self.ratings=ratings
    def display(self):
        print("Artistname = {}, Year of release = {}, Ratings = {}".format(self.artistname,self.year,self.ratings))
    def Add(self):
        self.artistname=input("Enter the artist name: ")
        self.year=int(input("Enter the year of movie release: "))
        self.ratings=float(input("Enter the ratings of the movie: "))
artistname=' '
year=0
ratings = 0
s1=MovieDetails(artistname,year,ratings)
s1.Add()
s1.display()


'''Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.'''
class Animal:
    def animal_attribute(self):
        print("In Animal_attribute")
class Tiger(Animal):
    def __init__(self):
        super().animal_attribute()
r=Tiger()


'''Q.6- What will be the output of following code.
class A:
        def f(self):
            return self.g()
        def g(self):
            return 'A'
class B(A):
    def g(self):
        return 'B'
a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())'''
#Output of the code first print statement is A B and second print statement is A B


'''Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.'''
class Shape:
    def __init__(self):
        self.length=0
        self.breadth=0
    def Area(self,l,b):
        self.length=l
        self.breadth=b
        print(self.length*self.breadth)
class rectangle(Shape):
    def __init__(self):
        self.l=int(input("Enter the length of rectangle: "))
        self.b=int(input("Enter the breadth of rectangle: "))
        print("Area of rectange =",end =' ')
        super().Area(self.l,self.b)
class square(Shape):
    def __init__(self):
        self.side=int(input("Enter the side of square: "))
        print("Area of square =",end =' ')
        super().Area(self.side,self.side)
r = rectangle()
s = square()
