with open("demo.txt", "r") as f:
    data=f.read()
    print(data)

with open("demo.txt", "a") as f:
    f.write(".\nHow are you?")

# It is important to note that I nedd no to close the file whiel using "with" syntax.