# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x_fba = 1 #int
y_fba = 2.5 #float
name_fba = feridun #str
is_cool = True #bool

x_fba, y_fba, name_fba, is_cool  = (1, 2.5, feridun, True)

print('Hello')

#basic math
a = x_fba + y_fba

print(type(x))
# casting
x_fba = str (x_fba)
y_fba = int(y_fba)
z_fba = float(y_fba)
print(type(y_fba), y_fba)
