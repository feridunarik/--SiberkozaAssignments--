# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_fba = ['ahmet', 'mehmet', 'feridun', 'berkin']

for person_fba in people_fba:
    print(f'Current Person: {person_fba}')
for person_fba in people_fba:
  if person_fba == 'ahmet':
    break
  print(f'Current Person: {person_fba}')

  for person_fba in people_fba:
  if person == 'ahmet':
    continue
     print(f'Current Person: {person_fba}')

  for i in range(len(people_fba)):
     print(people_fba[i])

  for i in range(0, 11):
     print(f'Number_fba: {i}') #goes until it hits 11




# While loops execute a set of statements as long as a condition is true.

count_fba = 0
while count_fba < 10:
  print(f'Count: {count_fba}')
  count_fba += 1
