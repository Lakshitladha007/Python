Documentation: https://requests.readthedocs.io/en/latest/

Generally, for passing parameters in a url we use this approach:<br>
"url": "https://httpbin.org/get?page=2&count=25"
But requests mdoule allows us to use a dictionary to define paramters and then we can pass them:<br>

```python
payload={'page':2, 'count':25}
response= requests.get('https://httpbin.org/get', params=payload)
```