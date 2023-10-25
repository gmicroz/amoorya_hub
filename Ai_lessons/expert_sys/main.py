import json

with open("amoorya_hub/Ai_lessons/expert_sys/db.json") as f:
    mapping = json.load(f)

print(json.dumps(mapping, indent=2))