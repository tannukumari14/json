import json
dict1 ={ "emp1": {"name": "Lisa","designation": "programmer","age": "34","salary": "54000"
},"emp2":{"name": "Elis","designation": "Trainee","age": "24","salary": "40000"},}
out_file = open("myfile.json", "w")
json.dump(dict1, out_file, indent = 3)
out_file.close()

# import json
# age='{"age":"12","salary":"20090}'
# print(json.dumps(age))