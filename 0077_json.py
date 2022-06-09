import json

with open('myinfo.json') as f:
    data = json.load(f)

print(data)

new_data = {
    "name": "월도",
    "birth": "0309",
    "age": 42
}
with open('myinfo.json', 'w') as f:
    json.dump(new_data, f)
    

json_data = json.dumps(new_data)
print(json_data)

json_data = json.dumps(new_data, ensure_ascii=False)
print(json_data)

print(json.loads(json_data))

print(json.dumps(new_data, indent=2, ensure_ascii=False))

print(json.dumps([1,2,3]))