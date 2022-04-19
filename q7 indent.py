import json
city=("indore","bihar","delhi","pune")
print(json.dumps(city))
print(json.dumps(city,indent=4))
print(json.dumps(city,separators=(".","|")))
