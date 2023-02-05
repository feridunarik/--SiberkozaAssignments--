# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_fba = 'Feridun'
age_fba = 21

#concatenate
print('Hello, my name is ' +name_fba+ ' and i am' +str(age))

# String Formatting

# arguments by position
print( 'My name is  {name} and I am {age}'.format(name=name_fba, age=age_fba))
# F-Strings
print(f'Hello, my name is {name_fba} and I am {age_fba}')

# String Methods
s_fba ='hello world'

#capitalize string
print(s_fba.capitalize())
print(s_fba.upper)
print(s_fba.lower)
print(s_fba.swapcase)
print(len(s_fba))
print(s_fba.replace('world', 'everyone'))
sub_fba = 'h'
print(s_fba.count(sub))
print(s_fba.startswith('hello'))
print(s_fba.endswith('d'))
print(s_fba.split())
print(s_fba.find('r'))
print(s_fba.isalnum())
print(s_fba.isalpha())
print(s_fba.isnumeric())
