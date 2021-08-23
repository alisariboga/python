#Functions
"""
What I Will Learn
Functions
Function parameters
Function documenttation
Returning data from a function
"""
"""Functions
DRY = Don't Repeat Yourself
Write one time, use many times
"""

#def function_name() :
	#Code Block

def say_hi() :
	print('Hi!')

say_hi()

def say_hi(name) :
		print('Hi {}!'.format(name))

say_hi('Ali')
say_hi('Sifa')


"""
say_hi()
File "say_hi.py", line 30, in <module>
	say_hi()
TypeError: say_hi() missing 1 required
positional argument: 'name'

"""

"""def say_hi(name = 'there'):
	print('Hi {}'.format(name))

say_hi()
say_hi('Jason')

def say_hi(first, last):
	print('Hi {} {}!'.format(first, last))

say_hi('Jane', 'Doe')
say_hi(first = 'Jane', last = 'Doe')
say_hi(last = 'Doe', first = 'John')


def say_hi(first, last='Doe'):
	print('Hi {} {}!'.format(first, last))

say_hi('Jane')
say_hi('John', 'Coltrane')
"""
#Part 2

# def say_hi(first, last='Doe'):
# 	"""Say hello."""
# 	print('Hi {} {}!'.format(first,last))

# help(say_hi)

def odd_or_even(number) :
	"""Determine if a number iss odd or even"""
	if number % 2 == 0:
		return 'Even'
	else:
		return 'Odd'

odd_or_even_string = odd_or_even(7)
print(odd_or_even_string)

def is_odd(number):
	"""Determine if a number is odd"""
	if number % 2 == 0:
		return False
	else:
		return True

print(is_odd(7))

def get_name():
	name = input('What is your name? ')
	return name

def say_name(name):
	print('your name is {}.' .format(name))

def get_and_say_name():
	"""Get and display name"""
	name = get_name()
	say_name(name)

get_and_say_name()











































