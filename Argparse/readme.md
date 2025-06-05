### Argparse Definition
argparse is a standard library module for parsing command-line options, arguments, and subcommands.<br>

### Purpose: Makes it easy to write user-friendly command-line interfaces.

#### Basic Workflow of argparse
1. Import argparse
2. Create parser object using argparse.ArgumentParser()
3. Add arguments with add_argument()
4. Parse the arguments using parse_args()
5. Use the parsed arguments

Example
```python
import argparse

# Step 1: Create the parser
parser = argparse.ArgumentParser(description="A simple example")

# Step 2: Add arguments
parser.add_argument("name", help="Your name")
parser.add_argument("--age", type=int, help="Your age", default=18)

# Step 3: Parse arguments
args = parser.parse_args()

# Step 4: Use arguments
print(f"Hello {args.name}, you are {args.age} years old.")
```

Run this script via CLI like:<br>
```bash
python script.py Lakshit --age 25
```
#### Important Functions & Features
| Function / Feature | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `ArgumentParser()` | Creates a new parser object                                         |
| `add_argument()`   | Defines the arguments the script accepts                            |
| `parse_args()`     | Parses command-line arguments into an object                        |
| `help`             | Automatically generated help messages                               |
| `type`             | Converts input to the specified type (e.g., `int`, `float`)         |
| `default`          | Sets a default value if the argument is not provided                |
| `required=True`    | Marks an optional argument as required                              |
| `choices=[...]`    | Limits values to specific options                                   |
| `nargs`            | Specifies number of command-line arguments (`?`, `*`, `+`, or int)  |
| `action`           | Specifies how to handle the argument (e.g., `store_true` for flags) |

#### Types of Arguments
| Type       | Example                          | Notes                                |
| ---------- | -------------------------------- | ------------------------------------ |
| Positional | `parser.add_argument("input")`   | Required and order matters           |
| Optional   | `parser.add_argument("--debug")` | Optional, usually prefixed with `--` |

##### Auto Help Message
Running this:
```bash
python script.py --help
```

Outputs:
```bash
usage: script.py [-h] [--age AGE] name

positional arguments:
  name        Your name

optional arguments:
  -h, --help  show this help message and exit
  --age AGE   Your age
```

#### Summary
> argparse is perfect for:
1. Building robust command-line tools
2. Automatically handling help messages
3. Enforcing data types and validations

### args and kwargs

#### What Are *args and **kwargs?
| Keyword    | Stands for           | Accepts                          |
| ---------- | -------------------- | -------------------------------- |
| `*args`    | Positional arguments | A **tuple** of unnamed arguments |
| `**kwargs` | Keyword arguments    | A **dict** of named arguments    |

### *args: Variable-Length Positional Arguments
> Used when we want to accept any number of positional arguments (not keywords).<br>

Example:
```python
def greet_all(*args):
    for name in args:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")
```
Output:
```bash
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```
#### args is a tuple: ('Alice', 'Bob', 'Charlie')

### **kwargs: Variable-Length Keyword Arguments
Used when we want to accept any number of keyword arguments (like key=value).<br>
Example:
```python
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, country="India")
```
Output:<br>
```bash
name: Alice
age: 25
country: India
```
#### kwargs is a dictionary: {'name': 'Alice', 'age': 25, 'country': 'India'}

### Rules of order:
```python
def func(fixed, *args, default=0, **kwargs):
    pass
```

#### Can be unoacked while calling a function:
```python
args = (1, 2)
kwargs = {"x": 10, "y": 20}
func(*args, **kwargs)
```