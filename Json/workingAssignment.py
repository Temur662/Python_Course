import requests
import json
nested_json_string = """{
  "name": "Alex",
  "age": 29,
  "contact": {
    "email": "alex@example.com",
    "phone": "123-456-7890"
  },
  "skills": ["Python", "Data Analysis", "Machine Learning"]
}"""

info = json.loads(nested_json_string)
print(info["name"])
info["age"] = 31
print(info["age"])

employee = """{"employee": {"name": "John Doe", "roles": ["Admin", "User"], "email": "johndoe@example.com"}}"""

employeeDict = json.loads(employee)

print(employeeDict["employee"]["name"], "Roles = ",employeeDict["employee"]["roles"])



