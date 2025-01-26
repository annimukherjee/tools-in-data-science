import json

# Input JSON array of objects
data = [
    {"name": "Alice", "age": 82},
    {"name": "Bob", "age": 50},
    {"name": "Charlie", "age": 8},
    {"name": "David", "age": 15},
    {"name": "Emma", "age": 49},
    {"name": "Frank", "age": 68},
    {"name": "Grace", "age": 66},
    {"name": "Henry", "age": 25},
    {"name": "Ivy", "age": 65},
    {"name": "Jack", "age": 30},
    {"name": "Karen", "age": 10},
    {"name": "Liam", "age": 96},
    {"name": "Mary", "age": 15},
    {"name": "Nora", "age": 72},
    {"name": "Oscar", "age": 8},
    {"name": "Paul", "age": 10}
]

# Sort by age first, and by name in case of a tie
sorted_data = sorted(data, key=lambda x: (x["age"], x["name"]))

# Convert back to JSON without spaces or newlines
sorted_json = json.dumps(sorted_data, separators=(',', ':'))
print(sorted_json)