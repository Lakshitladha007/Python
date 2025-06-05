## os Module – Traditional Path Handling

The os module provides a way to interact with the operating system — including path operations, file checks, and directory traversal.

#### Important Functions:
##### 1. os.path- Path Operations
| Function                 | Description                |
| ------------------------ | -------------------------- |
| `os.path.join(a, b)`     | Join paths                 |
| `os.path.exists(path)`   | Check if a path exists     |
| `os.path.isfile(path)`   | Check if it’s a file       |
| `os.path.isdir(path)`    | Check if it’s a directory  |
| `os.path.basename(path)` | File name from path        |
| `os.path.dirname(path)`  | Directory part of path     |
| `os.path.split(path)`    | Tuple of (dir, file)       |
| `os.path.splitext(path)` | Tuple of (file, extension) |
| `os.path.getsize(path)`  | Size of file in bytes      |
| `os.path.abspath(path)`  | Absolute path              |
| `os.path.normpath(path)` | Normalize path string      |

##### 2. os – File and Directory Operations
| Function              | Description                    |
| --------------------- | ------------------------------ |
| `os.mkdir(path)`      | Create a directory             |
| `os.makedirs(path)`   | Create nested directories      |
| `os.rmdir(path)`      | Remove empty directory         |
| `os.remove(path)`     | Delete a file                  |
| `os.rename(src, dst)` | Rename a file or folder        |
| `os.listdir(path)`    | List files in a directory      |
| `os.getcwd()`         | Get current working directory  |
| `os.chdir(path)`      | Change current directory       |
| `os.stat(path)`       | Get metadata (like size, time) |

##### 3. os.environ – Environment Variables
| Function                      | Description    |
| ----------------------------- | -------------- |
| `os.environ['VAR']`           | Access env var |
| `os.environ.get('VAR')`       | Safe access    |
| `os.environ['VAR'] = "value"` | Set env var    |

##### 4. os – Process and System Operations
| Function               | Description                                     |
| ---------------------- | ----------------------------------------------- |
| `os.system("command")` | Run shell command (less safe than `subprocess`) |
| `os.getpid()`          | Current process ID                              |
| `os.getlogin()`        | Logged-in username                              |
| `os.exit(n)`           | Exit script with status code                    |

<br>
<br>

##  pathlib Module – Modern Path Handling
pathlib uses object-oriented paths for cleaner and more readable code.

#### Important Methods:
| Method                        | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| `Path("path") / "child"`      | Join paths using `/`                            |
| `.exists()`                   | Check if path exists                            |
| `.is_file()` / `.is_dir()`    | File/directory checks                           |
| `.name` / `.stem` / `.suffix` | Get filename, name without extension, extension |
| `.parent` / `.parents`        | Get parent(s)                                   |
| `.mkdir()`                    | Create directories                              |
| `.unlink()`                   | Delete a file                                   |
| `.glob("*.txt")`              | Pattern-based file search                       |
