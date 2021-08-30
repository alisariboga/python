"""
What I will Learn
Creating
Deleting
Converting
Assignment
More built-in functions

#Tuple
A tuple is an immutable list
Tuples are ordered
Values accessed by index
Iteration, looping, concatenation
Use when data should not change


tuple_name = (item_1, item_2, item_N)
tuple_name = (item_1,)

"""

days_of_the_week = ('Monday','Tuesday', 'Wednesday',
 'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
	print(day)

#You cannot modify values in a tuple
# This will raise an exception

#days_of_the_week[0] = 'New Monday'

"""
Traceback (most recent call last):
  File "/Users/alisariboga/Desktop/python_course /9_truples/truples.py", line 34, in <module>
    days_of_the_week[0] = 'New Monday'
TypeError: 'tuple' object does not support item assignment
"""

# del days_of_the_week
# #This will raise an exception as the tuple was deleted.
# print(days_of_the_week)
"""
Traceback (most recent call last):
  File "/Users/alisariboga/Desktop/python_course /9_truples/truples.py", line 45, in <module>
    print(days_of_the_week)
NameError: name 'days_of_the_week' is not defined

Switching between Tuples and Lists

list() - Built-in function returns a list
tuple() - Built-in function returns a tuple
type() - Built-in function returns an onject's type
"""

weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
print('weekend_tuple is {}.'.format(type(weekend_tuple)))
print('weekend_list is {}.'.format(type(weekend_list)))

"""
weekend_tuple is <class 'tuple'>.
weekend_list is <class 'list'>.
"""

animals_list = ['man', 'bear', 'pig']
animals_tuple = tuple(animals_list)
print('animals_list is {}.'.format(type(animals_list)))
print('animals_tuple is {}.'.format(type(animals_tuple)))

"""
animals_list is <class 'list'>.
animals_tuple is <class 'tuple'>.

#Looping through a Tuple
for item_variable in tuple_name:
  # Code Block
"""

weekend_days = ('Saturday', 'Sunday')
for day in weekend_days:
  print(day)

"""
Saturday
Sunday
"""

weekend_days = ('Saturday', 'Sunday')
(sat, sun) = weekend_days
print(sat)
print(sun)

"""
Saturday
Sunday
"""
contact_info = ['555-0123', 'jason@example.com']
(phone, email) = contact_info
print(phone)
print(email)

"""
555-0123
jason@example.com
"""

def high_and_low(numbers):
  """Determine the highest and lowest number"""
  highest = max(numbers)
  lowest = min(numbers)
  return (highest, lowest)

lottery_numbers = [16, 4, 42, 15, 23, 8]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is: {}'.format(lowest))

"""
The highest number is: 42
The lowest number is: 4
"""

contacts = [('Jason', '555-0123'), ('Carl', '555-0987')]

for (name, phone) in contacts:
  print("{}'s phone number is {}.".format(name, phone))

"""
Jason's phone number is 555-0123.
Carl's phone number is 555-0987.
"""

#SUMMARY
"""
A tuple is an immutable list,
meaning once it is defined the values contained in the tuple cannot be changed.
Delete a tuple with the del statement
  #del tuple_name

Tuples can be converted to lists using the list() built-in function

Lists can be converted to tuples using the tuple() built-in function

You can use tuple assignment to assign values to multiple variables at once
(var_1, var_N) = (value_1, value_N)
Tuple assignment can be used in for loops

The max() built-in function returns the largest item that is passed to it
The min() built-in function returns the smallest that is passed to it
"""







































