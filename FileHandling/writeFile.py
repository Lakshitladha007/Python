f= open("demo.txt", "w") # basically, overwrites the current data in the file, if file does not 
                         # exist it creates a new file.

f.write("I want to learn javascript tomorrow.")

f.close()

f= open("demo.txt", "a") # it appends data to the file, if file does not exist it creates a new file.

f.write("\nIt is going to be amazing.")

f.close()