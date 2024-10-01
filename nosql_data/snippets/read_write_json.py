import json

data = json.loads(open("sample_data.json").read())
data.append({"country": "USA", "population": "331,002,651"})

print(json.dumps(data, indent=2))

print(json.dumps({"tuple": (1, 2, 3), "list": [1, 2, 3]}))