Python can be used to perform operations on files.

#### Types of files:
1. TEXT FILES: .txt, .log, .docx, etc.
2. BINARY FILES: .mp4, .mov, .png, .jpeg, etc.

Text files and binary files while accessing from python are different but in the end they are stored in the form of "bits" in the system( in the memory ).

### Open ,read and close a file:
Before reading a file, we need to open that file.
```python
f= open("file_path", "mode")<br>
```
The open function returns stream of data that the file contains.<br>
File modes in python:<br>
| Mode   | Description                                                  |
| ------ | ------------------------------------------------------------ |
| `'r'`  | Read (default). Error if file doesn’t exist                  |
| `'w'`  | Write. Creates file if not exists, **overwrites** if it does |
| `'a'`  | Append. Creates file if not exists, adds to end of file      |
| `'x'`  | Exclusive create. Fails if file exists                       |
| `'b'`  | Binary mode (used with `rb`, `wb`, etc.)                     |
| `'t'`  | Text mode (default, used with `r`, `w`, etc.)                |
| `'r+'` | Read and write                                               |

Bydefault, file open in read mode and in binary form.

To read data from while we use "read()" method:
1. To read particluar number of characters, we an use:
data = f.read(5)  // this will only read first 5 characters

2. line1= f.readline()
this reads first line of the file.


### Deleting a File
We can not delete file directly. We need to import "os" module.

```bash
import os
os.remove("filename")
```

#### Useful Methods:
| Method          | Description                  |
| --------------- | ---------------------------- |
| `.read()`       | Read entire file             |
| `.readline()`   | Read a single line           |
| `.readlines()`  | Read all lines into a list   |
| `.write()`      | Write to file                |
| `.writelines()` | Write a list of lines        |
| `.seek(offset)` | Move cursor to byte `offset` |
| `.tell()`       | Current cursor position      |


#### How to Convert Between Text and Binary
##### Text → Binary:
```python
text = "Hello"
binary = text.encode('utf-8')  # b'Hello'
```
##### Binary → Text:
```python
binary = b'Hello'
text = binary.decode('utf-8')  # 'Hello'
```
#### File copying using file handling
```python
with open("source.txt", "r") as src, open("backup.txt", "w") as dst:
    for line in src:
        dst.write(line)
```

#### Error handling:
```python
try:
    with open("/restricted/output.txt", "w") as f:
        f.write("Saving some data.")
except FileNotFoundError:
    print("⚠️ The directory doesn't exist.")
except PermissionError:
    print("⚠️ No write permission to this location.")
except Exception as e:
    print("⚠️ Unexpected error:", e)
finally:
    f.close()
```