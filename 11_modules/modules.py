"""
What I will learn
Modules
More built-in Python functions
Module search path
Python Standart Library

#Modules
Python modules are files that have a .py extension.
They can implement a set of attributes (variables), methods(functions), and classes(types).

A module can be included in another Python program by using the import nstatement followed by the module name.


import time 
time.method_name()
time.attribute_name
"""

import time
print(time.asctime())
print(time.timezone)

"""
Tue Aug 31 15:09:08 2021
0

#Modules
if you want single method 
---import module_name---
module_name.method_name()

from module_name import method_name
method_name()

"""
print('------------------------------------')
from time import asctime
print(asctime())
"""
0
Tue Aug 31 15:12:43 2021

from module_name import method_name
from module_name import method_name1, method_nameN
"""

# print('------------------------------------')
# from time import asctime, sleep
# print(asctime())
# sleep(3)
# print(asctime())
# print('------------------------------------')
# sleep(10)
# print(asctime())


"""
Tue Aug 31 15:17:10 2021
------------------------------------
Tue Aug 31 15:17:10 2021
Tue Aug 31 15:17:13 2021
------------------------------------
Tue Aug 31 15:17:23 2021

#Modules
sleep()
time.sleep()

#Don't do this!
from time import *
"""
# print('------------------------------------')
# from time import *
# print(timezone)
# print(asctime())
# sleep(3)
# print(asctime())
"""
0
Tue Aug 31 15:21:57 2021
Tue Aug 31 15:22:00 2021


#Module Search Path
sys.path - Returns the search path for modules

import sys
sys.path
"""
print('------------------------------------')
import sys
for path in sys.path:
	print(path)


"""
/Users/alisariboga/Desktop/python_course /11_modules
/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload
/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages

#PYTHONPATH Environment Variable
Mac/Linux:
PYTHONPATH = path1:pathN

Windows:
PYTHONPATH=path1;pathN
"""
"""
import say_hi
Traceback (most recent call last):
  File "/Users/alisariboga/Desktop/python_course /11_modules/modules.py", line 111, in <module>
    import say_hi
ModuleNotFoundError: No module named 'say_hi'


#Python Standard Library
#https://docs.python.org/3/library/
Python is distributed with a large library of modules
Check the Python standard library before writing any of your own code!
Just a few modules
	CSV
	logging
	urllib.request
	json
"""
print('------------------------------------')
import sys
file_name = 'test.txt'
try:
	with open (file_name) as test_file:
		for line in test_file:
			print(line)
except:
	print('Could not open {}.'.format(file_name))
	sys.exit(1)
"""
Deneme 123

Deneme 123
"""
# print('------------------------------------')
# def say_hi():
# 	print('Hi!')

# import say_hi
# say_hi.say_hi()

# print('------------------------------------')
# def say_hi():
# 	print('Hi!')

# print('Hello from say_hi2.py!')

# import say_hi2
# say_hi2.say_hi()

print('------------------------------------')
def say_hi():
	print('Hi!')

def main():
	print('Hello from say_hi3.py!')
	say_hi()

if __name__ == '__main__':
	main()
"""
Hello from say_hi3.py!
Hi!
"""
