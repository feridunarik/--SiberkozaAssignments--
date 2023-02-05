# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple
fruits_fba= ('Apples', 'Oranges', 'Grapes')
fruits2_fba = tuple (('Apples', 'Oranges', 'Grapes'))

fruits2_fba= ('Apples',)

print(fruits_fba[1])

del fruits2_fba #deletes
print(len(fruits_fba))
# fruits_fba[0] = 'Pears' Doesnt work

print(fruits2_fba, type(fruits2_fba)

# A Set is a collection which is unordered and unindexed. No duplicate members.

#create
fruits_set_fba = {'Apples', 'Oranges', 'Mango'}

#check if in set
print('Apples' in fruits_set_fba)
fruits_set_fba.add('Grapes')
fruits_set_fba.remove('Grapes')
fruits_set_fba.clear()
del fruits_set_fba
#dupplicates doesnt work
