"""
What I will Learn
Reading files
Writing to files
Opening and closing files
File object
String methods

Reading files, one line at a time
File modes
Line endings(Unix vs Windos)
Exceptions

#FILES
#Input and outpt
input() - Accept standart input
print() - Write standart output
Files are great for storage that lasts beyond the execution of a program.

open() - Built-in Function that opens a file and returns a file object.

open(path_to_file)

path_to_file - can be absolute or relative.

open('/var/log/messages')
open('log/messages')

open('C: \ Log \ Messages \ data.txt')
open('C:/Users/jason/Documents/python-notes.txt')
open('Documents/python-notes.txt')



"""
#File Objects (Stream Objects)

# hosts = open('/etc/hosts')
# hosts_file_contents = hosts.read()
# print(hosts_file_contents)

"""
Windows System
hosts = open('C:/Windows/System32/drivers/etc/hosts')
hosts_file_contents = hosts.read()
print(hosts_file_contents)

Copyright (c) 1993-2009 Microsoft Corp.

This is a sample HOSTS file used by MIcrosoft TCP/IP for Windows.

#File Position
read() - Returns the entire file.
seek(offset) - Change the current position to offset.
seek(0) - Go to the beginning of the file
seek(5) - Go to the 5th byte of the file.
tell() - Determine the current position in the file
"""

hosts = open('/etc/hosts')
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
print('----------------------')

print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
print('----------------------')

hosts.seek(0)
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
print('----------------------')
print('----------------------')
print('----------------------')

hosts = open('/etc/hosts')
print(hosts.read(3))
print(hosts.tell())


#Part II
print('-----------------------------')
hosts = open('/etc/hosts')
hosts_file_contents = hosts.read()
print(hosts_file_contents)
hosts.close()

print('-----------------------------')

hosts = open('/etc/hosts')
hosts_file_contents = hosts.read()
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:
	hosts.close()
print('File closed? {}'.format(hosts.closed))

"""
File closed? False
File closed? True
"""
"""
#Automatically Closing A File

with open(file_path) as file_object_variable_name:
	# Code BLock
"""

print('-------------------------')
print('Started reading the file.')
with open('etc/hosts') as hosts:
	print('File closed? {}'.format(hosts.closed))
	print(hosts.read())
print('Finished reading the file.')
print('File closed? {}'.format(hosts.closed))

"""
Started reading the file.
File closed? False

Finished reading the file.
File closed? True
"""

print('-------------------------')

#This is line one
#This is line two
#Finally, we are on the third and last line of the file

with open('file.txt') as the_file:
	for line in the_file:
		print(line)
"""
This is line one

This is line two

Finally, we are on the third and last line of the file
"""

print('-------------------------')

with open('file.txt') as the_file:
	for line in the_file:
		print(line.rstrip())
"""
This is line one
This is line two
Finally, we are on the third and last line of the file
"""
"""
File Modes
open(path_to_file, mode)
Mode 		Description
r 			Open for reading(default)
w 			Open for writing, truncating first
x 			Create a ne file and open it for writing
a 			Open for wrting, appending to file
File Modes, continued
Mode 		Description
+			Open a file for updating(read/write)
b 			Binary mode
t 			Text mode(default)

open('/pics/cat.jpg', rb)

"""
print('-------------------------')
#Checking the file mode
with open('file.txt') as the_file:
	print(the_file.mode)
#r
print('-------------------------')

with open('file2.txt', 'w') as the_file:
	the_file.write('This text will be written to the file.')
	the_file.write('Here is more text.')

with open('file2.txt') as the_file:
	print(the_file.read())
"""
This text will be written to the file.Here is more text.
"""

"""
Carriage Returns and Line Feeds
\r Carraige Return
\n New Line

\n Unix/Linux/Mac libe endings
\r\n Windows style line endings
"""
print('-------------------------')

with open('file2.txt', 'w') as the_file:
	the_file.write('This text will be written to the file. \n')
	the_file.write('Here is more text. \n')

with open('file2.txt') as the_file:
	print(the_file.read())

"""
This text will be written to the file. 
Here is more text. 
"""
print('-------------------------')

#Binary Files
with open('cat.jpg', 'rb') as cat_picture:
	cat_picture.seek(2)
	cat_picture.read(4)
	print(cat_picture.tell())
	print(cat_picture.mode)
"""
6
rb
"""
print('-------------------------')

#Open a file and assign its contents to a variable.
# If the file is unavailable, create an empty variable.

try:
	contacts = open('contacts.txt').read()
except:
	contacts = ''

print(len(contacts))













