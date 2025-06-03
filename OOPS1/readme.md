## Constructors in Python
In Python, a constructor is a special method used to initialize objects. It is defined using the __init__ method.<br>
All classe have a function called __init__, which is always executed when the Object is being initiated.<br>
The first parameter of __init__ is used to refer to the object that we are creating and generaly referred using "self", we can name it something else also.<br>
The self parameter is a reference to the current instance of the class, and is used to access vvariables that belong to the class.<br>

##### Basic Syntax:<br>
```python
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```

#### __init__ is automatically called when an object is created.
#### self refers to the current object.

We can pass parameters to set up initial state.<br>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self): # method
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
    
# Create an object
p = Person("Alice", 25)
p.greet()
```
##### Internally, self and object instance (P) are same thing.

#### Pass
Pass is a placeholder statement in Python that means “do nothing”. It’s used when you need a syntactically valid block but don’t want it to do anything yet.

Example:
```python
class Student:
    def __init__(self):
        pass
```

### Types of Constructor:
1. default constructor

2. parameterized constructor => They contain parameters other than self.<br>

I we won't define default constructor it will be automatically defined.<br>

### Class attributes and object (instance) attributes:

1. Class Attributes
> Belong to the class itself, not any one instance.<br>
> Shared across all instances of the class.<br>
> Defined outside of any method, typically at the top of the class.<br>
> Are stored once in memory.

Example:
```python
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name):
        self.name = name  # Object attribute

dog1 = Dog("Buddy")
dog2 = Dog("Charlie")

print(dog1.species)  # Canine
print(dog2.species)  # Canine
```
Here, All Dog instances share the species attribute.

2. Object (Instance) Attributes
> Belong to a specific object.
> Created inside the __init__ method (or other instance methods).
> Each object gets its own copy of these.

Example:
```python
dog1.name = "Buddy"      # Only dog1 has this name
dog2.name = "Charlie"    # Only dog2 has this name
```
Changing dog1.name doesn't affect dog2.name.<br>

#### Important Behavior
If you assign a value to a class attribute via an instance, Python will create a new instance attribute with the same name:

```python
class Example:
    val = 10  # class attribute

obj = Example()
print(obj.val)  # 10 (class attribute)

obj.val = 20    # now creates an object attribute 'val'
print(obj.val)  # 20 (object attribute)

print(Example.val)  # Still 10
```

#### Best Practices
1. Use class attributes for constants or shared data(e.g., a counter, default settings).
2. Use object attributes for per-instance data(e.g., name, age, etc.).

### Methdos in a class
Yes, in most instance methods, it's necessary to pass self as the first parameter.<br>

##### What is self in Python?
1. self represents the instance of the class.
2. It is how Python gives access to the attributes and methods of a class in object-oriented programming.
3. It must be the first parameter of instance methods.
4. Example: Using self
```python
class Student:
    def __init__(self, name):
        self.name = name  # refers to the instance variable

    def greet(self):
        print(f"Hello, my name is {self.name}")
```

> __init__ and greet both take self so they can work on that specific object.

##### What if you don’t use self?

```python
class Student:
    def greet():
        print("Hi")
```
Then calling Student().greet() will give an error:
"TypeError: greet() takes 0 positional arguments but 1 was given
Because Python automatically passes the instance (self) when you call it on an object."

#### Exceptions: When self is not required
1. @classmethod
Uses cls instead of self:<br>

```python
class Example:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1
```
2. @staticmethod
No self or cls:<br>

```python
class Example:
    @staticmethod
    def say_hello():
        print("Hello!")
```

#### Static Methods:
A static method is a method inside a class that:<br>
1. Does NOT take self or cls as the first argument.
2. Does NOT access instance (self) or class (cls) variables.
3. Is used to perform utility functions related to the class — but not dependent on object or class state.
4. Example:
```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

print(Temperature.celsius_to_fahrenheit(0))   # 32.0
print(Temperature.fahrenheit_to_celsius(100)) # 37.777...

```
