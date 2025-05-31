import requests

# get request
payload={'page':2, 'count':25}
response= requests.get('https://httpbin.org/get', params=payload)

# post request
data= {'name':'lakshit', 'password':'admin1234'}
response= requests.post('https://httpbin.org/post', data=data)
res=response.json()
# print(res)
# print(res['form'])

# basic Auth
r=requests.get("https://httpbin.org/basic-auth/corey/testing", auth=('corey', 'testing'))
print(r.text)

# delay reponse on time stamp

responsedelay= requests.get("http://httpbin.org/delay/1", timeout=3)
print(responsedelay)

responsedelay2= requests.get("http://httpbin.org/delay/4", timeout=3)
print(responsedelay2)