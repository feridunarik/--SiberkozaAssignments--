# Python has functions for creating, reading, updating, and deleting files.


myFile = open('myfile_fba.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed : ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('I love python')
myFile.write(' and C++')
myFile.close()

myFile = open('myfile_fba.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

myFile = open('myfile_fba.txt', 'r+')
text = myFile.read(100)
print(text)