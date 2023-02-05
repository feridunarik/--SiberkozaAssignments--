# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

#create
person_fba = {
    'first_name': 'Feridun'
    'last_name': 'Arik'
    'age' : 21
    }

#use constructor
person2_fba = dict(first_name='Feridun', last_name='Arik')

#get value
print(person_fba['first_name'])
print(person_fba.get('last_name'))
person_fba['phone'] = '111-111-11-11'
print(person_fba.keys())

print(person_fba.items())
person2_fba = person_fba.copy()
person2_fba['city'] = 'Boston'

del(person_fba['age'])
person_fba.pop('phone')
person_fba.clear()
print(len(person2_fba))
people = [
    {'name': 'Feridun', 'age': 21}
    {'name' : 'Ahmet', 'age': 25}
    ]
print(person_fba[1]['name'])