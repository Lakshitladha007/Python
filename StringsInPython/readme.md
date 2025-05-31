## STRINGS

### 1. String Creation
> In Python, there is no functional difference between '''triple single quotes''' and """triple double quotes""".<br>

> Both are used for:<br>
1. Multi-line strings
2. Docstrings (documentation for functions, classes, etc.)
3. Strings that contain both single (') and double (") quotes

#### The usecase where both differes is choosing based on quotes inside the string
1. Use triple double quotes if your string contains single quotes:
```python
msg = """It's a beautiful day."""
```
2. Use triple single quotes if your string contains double quotes:
```python
msg = '''He said, "Hello!"'''
```

### 2. String Operation
Some common string operation are:<br>
| Operation     | Example              | Result          |
| ------------- | -------------------- | --------------- |
| Concatenation | `'Hello' + ' World'` | `'Hello World'` |
| Repetition    | `'Hi' * 3`           | `'HiHiHi'`      |
| Indexing      | `'Python'[0]`        | `'P'`           |
| Slicing       | `'Python'[1:4]`      | `'yth'`         |
| Length        | `len('Python')`      | `6`             |
| Membership    | `'th' in 'Python'`   | `True`          |

### 3. String Methods:
Some of the basic string methods are:
```python
s = " hello world "

print(s.upper())        # ' HELLO WORLD '
print(s.lower())        # ' hello world '
print(s.strip())        # 'hello world'
print(s.replace("world", "Python"))  # ' hello Python '
print(s.split())        # ['hello', 'world']
print(s.startswith(" h"))  # True
print(s.endswith("d "))    # True
```

### 4. String formatting

#### 1. f-strings:
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```
#### 2. .format() method:
```python
print("My name is {} and I am {} years old.".format(name, age))
```

##### In Python, strings are immutable, which means you cannot change a string after it is created. However, you can create new strings based on operations or transformations on the original string.