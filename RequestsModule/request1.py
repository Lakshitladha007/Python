import requests
response= requests.get("https://www.geeksforgeeks.org/convert-bytes-to-bits-in-python/")
print(response.text) #we get a response object with status code
# we can view what are the attributes and functions available with this object 
# using "dir()"
# We can also use "help", it gives a lot more detailed explaination
# print(dir(response))
# print(help(response))