import json

def task(path):
    with open(path, "r") as f:
        data = json.load(f)
        return round(sum(item["score"] * item["weight"] for item in data), 3)

print(task("input.json"))
