
# loads, dumps
import json
import requests

with open('file_manipulation/file.json', 'r') as f:

    data = json.load(f)
    print(type(data))

new_data = [
    {"name": "bob", "age": "34"},
    {"name": "bold", "age": "34"}
]

with open('file_manipulation/file.json', 'w') as f:
    json.dump(new_data, f)
