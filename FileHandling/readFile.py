f= open("file.txt","r")

data2=f.read(6)
print(data2)

data=f.read()
print(data)

f.close()

f=open("file.txt", "r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)
f.close()