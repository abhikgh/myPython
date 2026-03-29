print("Hello World")
x = 5;
x = x+5;
print(x);
#This is a comment

print("Hello World.", end=" ")
print("I will print on the same line.", end =" ")
print("I will print on the same line again")
print("Print in new line", 10, "lines")
"""
Multi line comments
How is that
"""
x = 5
y = "John"
print(type(x))
print(type(y))

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


x = "awesome"

def myfunc(x):
    x = x + ",fantastic"
    print("Python is " + x)

myfunc(x)



"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

import random

print(random.randrange(1, 10)) #from 1 to 9

y = int(2.8) # y will be 2

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5]) #llo
print(b.upper()) #HELLO, WORLD!

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

print(bool("Hello"))  #true
print(bool(15))      #true
bool(0)  #false
bool("") #false

x = 12
y = 5
print (x/y)
print (x//y)

#Walrus Operator :=
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")  #List has 5 elements

#is - Checks if both variables point to the same object in memory
#== - Checks if the values of both variables are equal
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # true
print(x is y) # false
print(x == y) # true

list1 = ["abc", 34, True, 40, "male"]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # ['orange', 'kiwi', 'melon']

#Change list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  #change
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #change
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # ["apple", "banana"] , If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
thislist.reverse()
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]


# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1]="yellow"
# Add "purple" to the end
colors.append("purple")
# Remove "red"
colors.remove("red")
# Print the list
print(colors)

# Tuple: immutable, ordered, Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# Tuple allow duplicate values

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) # ("apple", "kiwi", "cherry")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple) # ('apple', 'banana', 'cherry', 'orange')

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
"""
apple
banana
['cherry', 'strawberry', 'raspberry']
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
"""
apple
['mango', 'papaya', 'pineapple']
cherry
"""

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Create the tuple
fruits = ("apple", "banana", "cherry")
# Print the second item
print(fruits[1])
# Print the number of items
print(len(fruits))
# Unpack the tuple
(a,b,c)=fruits
# Print b
print(b)

#Set :  unordered, unchangeable*, unindexed
thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset) #{True, 2, 'banana', 'cherry', 'apple'}
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]
thisset.update(tropical)
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")   # DNE : error
#or
thisset.discard("banana")   # DNE : no error
print(thisset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3) #{2, 'c', 1, 3, 'a', 'b'}

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)  #apple

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)   #apple

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) # "banana" , "cherry"

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) # {'google', 'banana', 'microsoft', 'cherry'}

# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"
colors.discard("green")
# Print the number of items
print(len(colors))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
del thisdict["model"]
# or thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Create the dictionary
car={
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 2024
}
# Print the model
print(car['model'])
# Add a color key
car['color']="red"
# Remove the brand key
#del car['brand']
car.pop('brand')
# Print the dictionary
print(car)

age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

a = 5
b = 2
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
bigger = a if a > b else b
print("A") if a > b else print("=") if a == b else print("B")
#if a > b and c > a:
# print("Both conditions are True")
#if (age < 18 or age > 65) and not is_student or has_discount_code:
# print("Discount applies!")

value = 50
if value < 0:
    print("Negative value")
elif value == 0:
    pass # Zero case - no action needed
else:
    print("Positive value")

# Create age variable
age=20
# Write if/elif/else
if age<13 :
    print("Child")
elif age<18 :
    print("Teenager")
else :
    print("Adult")

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")


month = 4
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")


# Create variable day
day=3
# Use match statement
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# Create the i variable
i=0
# While loop: print 1-5, skip 3 with continue
while i < 6 :
    i += 1
    if i==3 :
        continue
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(6): #0-5
    print(x)
else:
    print("Finally finished!")


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def my_function(name = "friend"): #default parameter
    print("Hello", name)


def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)  #My dog's name is Buddy
    print("My"+ animal + "'s name is"+ name)  #Mydog's name isBuddy

my_function(animal = "dog", name = "Buddy")


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


def my_function(name, /): #Positional argument only
    print("Hello", name)
my_function("Emil")
#my_function(name = "Emil") #Keyword argument not allowed

#*args  = If the number of arguments is unknown, add a * before the parameter name:
#**kwargs = Keyword Arguments
def my_function(*, name):
    print("Hello", name)
my_function(name = "Emil") #Keyword argument only
#my_function("Emil")  #Positional argument not allowed

def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*kids):  #varargs
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def my_function(**kid):  #tuple
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
"""
Title: User Info
Positional arguments: ('Emil', 'Tobias')
Keyword arguments: {'age': 25, 'city': 'Oslo'}
"""

def my_function(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # If you have values stored in a list, you can use * to unpack them into individual arguments:
print(result) #6


def my_function(fname, lname):
    print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")


x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x) #200


x = 300
def myfunc():
    x = 200
myfunc()
print(x) #300

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())

"""
Lambda Functions
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression

"""
x = lambda a: a + 10
print(x(5))  #15

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
#[2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
#students = [("Tobias", 22),("Emil", 25),("Linus", 28)]

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

"""
Generators
Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.
"""
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)  # 1 2 3

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num) # 1 2 3 4 5


def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
#Emil Tobias Linus

# Create the greet function
def greet(name) :
    print("Hello", name);
# Call greet
greet("Emil")

for i in range(10):
    print(i)

# Print 0 through 5
for i in range(6):
    print(i)

# Print 2 through 5
for i in range(2,6):
    print(i)


# Create a list
cars = ["Ford", "Volvo", "BMW"]
# Print the first item
print(cars[0])
# Change the second item to "Toyota"
cars[1]="Toyota"
# Print the list
print(cars)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Create a tuple
mytuple = ("apple", "banana", "cherry")
# Create an iterator
myit = iter(mytuple)
# Print the first item
print(next(myit))

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


x = -1
#if x < 0:
# raise Exception("Sorry, no numbers below zero")

x = "hello"
#if not type(x) is int:
# raise TypeError("Only integers are allowed")

# Try to print x
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("Execution complete")


price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59.9099
txt = f"The price is {price:.2f} dollars"
print(txt) #59.91

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}" #Cheap

print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price = 59000
txt = f"The price is {price:,} dollars" #59,000 comma is a thousand separator
print(txt)

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# Create a variable
price=49
# Create an f-string
txt=f"Test its value {price}"
# Print the result
print(txt)

x = None
print(type(x))  #NoneType

# Assign None to x
x=None
# Check if x is None
if x is None:
    print("x is None")

print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")


import math

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")


y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")

f = open("demofile.txt", "rt")
print(f.read())
print(f.read(5))
print(f.readline())
f.close()

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

#f = open("D:\\myfiles\welcome.txt")
#print(f.read())

with open("demofile.txt") as f:
    print(f.read())

with open("demofile.txt") as f:
    for x in f:
        print(x) # loop line by line

with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())


with open("demofile.txt", "w") as f:  #w overwrites existing content
    f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())

#Inheritance
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

# Create the Animal class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name)

# Create the Dog class (inherits from Animal)
class Dog(Animal):
    pass

# Create an object
d1 = Dog("Rex")
# Call the speak method
d1.speak()



