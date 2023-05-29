# Json
import json
person = {"name": "John", "age": 30, "City": "New York", "hasChildren": False, "Titles": ["Engineer","Programmer"]}
personJSON = json.dumps(person, indent=4)
print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
#Decoding
with open('personJSON', 'r') as file:
    person = json.loads(file)
    print(person)