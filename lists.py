# A List is a collection which is ordered and changeable. Allows duplicate members.

#create list
numbers_fba = [1, 2, 3, 4, 5]
fruits_fba = ['Apples', 'Oranges', 'Grapes', 'Pears'] 

# constructor
numbers2_fba = list((1, 2, 3, 4, 5))

#get a value
print(fruits_fba[1])

#get length
print(len(fruits_fba))



fruits_fba.append('Mangos')

fruits_fba.remove('Grapes')

fruits_fba.insert(2, 'Strawberries')

fruits_fba[0]= 'Blueberries'

fruits_fba.pop(2)

fruits_fba.reverse()

fruits_fba.sort()

fruits_fba.sort(reverse=True)


print(fruits_fba)

