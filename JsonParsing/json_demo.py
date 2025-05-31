''' JSON=> Javascript Object Notation'''
''' Json library is part of standard libraries, no need to install them separately'''
import json

people_string='''
{
  "people": [
  {
    "name":"lakshit",
    "age":"22",
     "emails":"abc@gmail.com",
     "has_license":true
  },
  {
    "name":"rohit",
    "age":"25",
     "emails":null,
     "has_licence":false
  }]
}
'''

data = json.loads(people_string)
print(data)
# It can be observed, 'null' gets converted to None, true to True, false to False.
print(type(data))
print(type(data['people'])) 
# people is an array, it gets converted to List.

print("Printing the people's list\n")
for people in data['people']:
    print(f'{people}')

print("Printing the people's name from the list\n")
for people in data['people']:
    print(f'{people['name']}')

