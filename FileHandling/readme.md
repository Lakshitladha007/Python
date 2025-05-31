Python can be used to perform operations on files.

#### Types of files:
1. TEXT FILES: .txt, .log, .docx, etc.
2. BINARY FILES: .mp4, .mov, .png, .jpeg, etc.

Text files and binary files while accessing from python are different but in the end they are stored in the form of "bits" in the system( in the memory ).

### Open ,read and close a file:
Before reading a file, we need to open that file.

f= open("file_path", "mode")<br>
The open function returns stream of data that the file contains.<br>
Possible modes of file handling:<br>
1. read(r)
2. write(w), it overwrites the previous present data
3. (x) open a newfile and open it for writing
4. (a) open for writing and if file exits append at the end
5. (b) binary mode
6. (+) open a disk for updating(reading and writing)

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