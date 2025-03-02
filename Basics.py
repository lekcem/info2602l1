#This is a comment

x = 11 #initialization
x = 63 #assignment
y = 0 #declaration
z = (x + y)/x + (78%3) #usual mathematical operations supported 

#------------------Variable types-----------------
name = "Jeff" #string
age = 20 #integer
height = 6.5 # float
hasDate = False
comp = 7j #complex

# using fstrings for interpolation
message = f'Hi my name is {name} I am {age} years old'
print(message) # ‘Hi my name is Jeff I am 20 years old'

# type casting to convert types
intHeight = int(height) # 6
strHeight = str(height) # '6'
floatHeight = float(intHeight) # 6.0 
ageType = type(age)

name  = input("Enter your name: ") # reads input
print (name) # prints output

#------------------IF Statements-----------------
if 3 > 5:
  print("more")
else :
 print("less")
 
# elif === else if
mark = input("Enter mark: ")
mark = int(mark)
if mark > 70 :
  print("A")
elif mark > 60:
  print("B")
elif mark > 50:
  print("C")
else :
  print("F") 

#------------------Iteration-----------------
i = 1
while i < 10:
 print(i)
 i+=1
else:
 print("This is run when the loop condition is no longer met")

# iterating an iterable such as a list
list = ["bob", "sally", "john"]
for j in list:
 print(j)

# iterating between custom range an increment
for i in range(0, 10, 2):
 print(i)
 
 
 #------------------Functions-----------------
 #basic function
def add(a, b):
        return a + b

def printPerson(name, age, height):
        print(name, age, height)

# you can specify arguments in any order if they are named
printPerson(age=12, name='bob', height=5);

#default arguments are used when they are not given in the function call
def sayHello(fname, lname='Smith'):
        print('Hello '+fname + ' ' + lname)

sayHello('John');

sayHello('Bill', 'Young');

# functions can return multiple values

#------------------Lists-----------------
list = ['item1', 'item2', 'item3']
list2 = [12, 33, 45, 58, 23]

print(list);
# negative indexing can access elements starting from the end
print(list2[-1])

# select a subset of a list
print(list2[2:4])

# gets the length of a list
print(len(list2))

#add items to list
list.append('item4');

#remove item from list
item4 = list.pop()

#copy list
list3 = list2.copy()

# list comprehension, lets you create new lists from existing lists

num = [ 1, 2, 3, 4]
doubled = [n*2 for n in num]
print(doubled) # [ 2, 4, 6, 8]
odd = [ n for n in num if n%2 == 1]
print(odd) # [ 1, 3]

# unpacking a list, lets you create variables from items in the list
num = [ 1, 2, 3, 4]
[first, second, *rest] = num
print(first)
print(second)
print(rest)
# joining lists
num2 = [5, 6]
num3 = num + num2
print(num3) # [1, 2, 3, 4, 5, 6]

# copying lists
num4 = num2.copy()

#------------------Tuples-----------------
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple); # ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple[0]); # ‘apple'


#------------------Sets-----------------
data = [ 20, 3, 20, 42, 2, 3, 10, 32, 2]

myset = {0, 1}

for num in data:
 myset.add(num)

print(myset)# {0, 1, 2, 3, 32, 42, 10, 20}
num_unique = len(myset)

#------------------Dictionary-----------------
mydict = {
        "name":"bob",
        "age": 34
}

print(mydict)

# assessing a key
print(mydict['age'])

# adding a new key and value
mydict['height'] = 7

# iterating keys
for key in mydict:
        print(key)

# iterating values
for key in mydict:
        print(mydict[key])

# check for a key
if 'weight' in mydict:
        print(mydict['weight'])
else:
        print('no weight property!')
        
        
#------------------Classes-----------------
#Parent class
class Person:

  def __init__(self, name, height, weight):
    self.name = name;
    self.height = height;
    self.weight = weight;

  def sayHello(self):
    print("Hello! I'm a person, my name is", self.name)

# Child class inherits from Person
class Student(Person):

        # super is the reference to the parent class Person so 
        # we call Person's constructor here to set the Person
        # properties of the student instance
        def __init__(self, stid, name, height, weight):
                super().__init__(name, height, weight)
                self.stid = stid
        
        # override method of parent
        def sayHello(self):
                print("Hello! I'm a student, my name is", self.name)


bob = Person('bob', 12, 34)
sally = Student(123, 'sally', 7, 34)

bob.sayHello();
sally.sayHello();

print(bob.name);