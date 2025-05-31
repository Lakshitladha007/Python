import os

# print(dir(os)) # simplies print all the available methods with OS module

pwd=os.getcwd()
print(pwd)

# os.chdir("C:\cprogramming\PYTHON")
# print(os.getcwd())

print(os.listdir()) 

# os.mkdir("users")
# os.makedirs("students/lakshit")

# os.rmdir("users")
# os.removedirs("students/lakshit")
os.rename('demo_os.py','os.py')