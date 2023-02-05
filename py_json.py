# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

user_fbaJSON = '{"first_name_fba": "feridun", "last_name_fba": "arik", "age_fba": 21}' #mind the double quotes

user_fba = json.loads(userJSON)

print(user_fba)
print(user_fba['first_name_fba'])

car_fba = {'make_fba': 'Ford_fba', 'model_fba': 'Mustang_fba', 'year_fba': 1970}

car_fbaJSON = json.dumps(car_fba)

print(car_fbaJSON)