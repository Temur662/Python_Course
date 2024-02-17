import json
import requests
dataFile = open("data.json", )
#loads for string load .json file
theData = json.load(dataFile)
print(theData)

newData = {
    "Hobby": "Soccer",
    "Country" : "Uzbekistan"
}

theData.update(newData)
print(theData)


with open("data.json", 'w') as json_file:
    json.dump(theData, json_file, indent = 4)