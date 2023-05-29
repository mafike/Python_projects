# Json
# how t encode and decode an object code
import json
class User:
    def __int__(self, name, age):
        self.name = name
        self.age = age
user = User('Max', 27)
def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')
from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True }
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, default=encode_user)
print(userJSON)