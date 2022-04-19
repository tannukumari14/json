import json
a='{"name":"tanu","friends":sneha}'
data=json.loads(a)
print(data.get("friends"))