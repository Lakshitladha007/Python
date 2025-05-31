## OS module

### What is the os Module?
The os module in Python is a standard library module that provides a way of interacting with the operating system.<br>
It allows you to perform tasks related to file and directory handling, process management, environment variables, and more.

### Why is it Used?
The os module is used when you want your Python program to:
1. Work with the file system (create, delete, rename files/directories).
2. Access environment variables.
3. Run system commands.
4. Manage paths and directories.


### Common Uses of os Module
##### 1. Working with Directories and Files
```BASH
import os

# Get current working directory
print(os.getcwd())

# List contents of a directory
print(os.listdir())

# Create a directory
os.mkdir("new_folder")

# Remove a directory
os.rmdir("new_folder")
```
##### 2. Path Handling
```BASH
# Join paths safely (cross-platform)
path = os.path.join("folder", "file.txt")
print(path)

# Check if a file or directory exists
print(os.path.exists(path))

# Get file name and directory name
print(os.path.basename(path))  # file.txt
print(os.path.dirname(path))   # folder
```
##### 3. Environment Variables
```BASH
# Get environment variable
user = os.getenv("USER")  # or "USERNAME" on Windows
print(user)
```
##### 4. Running System Commands
```BASH
# Run a shell command
os.system("echo Hello, World!")
```

| Feature                    | Purpose                               |
| -------------------------- | ------------------------------------- |
| `os.getcwd()`              | Current working directory             |
| `os.listdir()`             | List files in a directory             |
| `os.mkdir()`, `os.rmdir()` | Create and remove directories         |
| `os.path.join()`           | Combine paths in a cross-platform way |
| `os.path.exists()`         | Check if a file or directory exists   |
| `os.getenv()`              | Access environment variables          |
| `os.system()`              | Run shell/system commands             |


#### os.walk()
The os.walk() function in Python's os module is used to generate the file names in a directory tree by walking either top-down or bottom-up. It's especially useful when you want to iterate over all files and directories in a given directory, including subdirectories.

> Syntax:
```bash
os.walk(top, topdown=True, onerror=None, followlinks=False)
```
> Parameters:
1. top: The root directory from which to start walking.
2. topdown (default=True):
3. If True, directories are scanned from top to bottom.
4. If False, it scans from the bottom up.
5. onerror: Optional function that gets called with an OSError instance if an error occurs.
6. followlinks: If True, follows symbolic links to directories.

> Return Value:
It yields a 3-tuple for each directory in the tree:(dirpath, dirnames, filenames)<br>
1. dirpath: the current path.
2. dirnames: list of directories in dirpath.
3. filenames: list of non-directory files in dirpath.

🔹 Example Usage:
```bash
import os

for dirpath, dirnames, filenames in os.walk("my_folder"):
    print(f"Current path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}")
    print("-" * 30)
```
> Example: Find  all files that ends with ".txt"
```bash
import os

for root, dirs, files in os.walk("documents"):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
```