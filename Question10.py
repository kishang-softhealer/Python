# Question 10: Parse JSON and Check Keys
import json
d_json = '{"name": "Alice", "age": 25}'

d_python = json.loads(d_json)
print(type(d_python))
print(d_python)

for i in d_python.keys():
   if i in d_python:
     dic_json = json.dumps(d_python)
print(type(dic_json))
print(dic_json)
