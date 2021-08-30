#What you will learn
""" 
Lists
Searching in Lists
Exception Handling
Slices
Ranges
For Loop
While Loop

#Lists
A list is a data type that holds an ordered collection of items.
The items can be of varrious data types
You can even have lists of lists!


list_name = [item_1, item_2, item_N]
list_name = []
list_name[index]


"""

animals = ['man', 'bear', 'pig']
print(animals[0])
animals[0] = 'cat'
print(animals[0])

animals = ['man', 'bear', 'pig']
print(animals[-1])
print(animals[-2])
print(animals[-3])

animals = ['man', 'bear', 'pig']
animals.append('cow')
print(animals[-1])

animals = ['man', 'bear', 'pig']
animals.extend(['cow','duck'])
print(animals)

more_animals = ['horse', 'dog']
animals.extend(more_animals)
print(animals)


animals = ['man', 'bear', 'pig']
animals.insert(0, 'horse')
print(animals)

animals.insert(2, 'duck')
print(animals)

"""
#Slices
list[index1:index2]
list[:index2]
list[index1:]

"""
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']


some_animals = animals[1:4]
print('Some animals:        {}'.format(some_animals))

first_two = animals[0:2]
print('First two animals: {}' .format(first_two))

first_two_again = animals[:2]
print('First two animals: {}'.format(first_two_again))


animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

last_two = animals[4:6]
print('last two animals:    {}'.format(last_two))

last_two_again = animals[-2:]
print('last two animals:    {}'.format(last_two_again))

part_of_a_horse = 'horse'[1:3]
print(part_of_a_horse)


"""
#Exception Handling
Finding an item in a list
"""
animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
print(bear_index)

# animals = ['man', 'bear', 'pig']
# cat_index = animals.index('cat')
# print(cat_index)

"""
Traceback (most recent call last):
  File "/Users/alisariboga/Desktop/python_course /Section_7/lists.py", line 95, in <module>
    cat_index = animals.index('cat')
ValueError: 'cat' is not in list
"""
animals = ['man', 'bear', 'pig']
try:
	cat_index = animals.index('cat')
except:
	cat_index = 'No cats found'
print(cat_index)
#No cats found

"""
#loops
for item_variable in list_name:
	# Code block

item_variable = list[0]
item_variable = list[1]
item_variable = list[N]
"""

animals = ['man', 'bear', 'pig']
for animal in animals:
	print(animal.upper())

#MAN
#BEAR
#PIG

"""
#While Loop
while condition
	# Code block
"""
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']

index = 0

while index < len(animals):
	print(animals[index])
	index += 1
"""
man
bear
pig
cow
duck
horse

# Sorting and Ranges
"""
animals = ['man', 'bear', 'pig']
sorted_animals = sorted(animals)
print('Animals list:			{}'.format(animals))
print('Sorted animals list: 	{}'.format(sorted_animals))
animals.sort()
print('Animals after sort method: {}'.format(animals))

"""
Animals list:			['man', 'bear', 'pig']
Sorted animals list: 	['bear', 'man', 'pig']
Animals after sort method: ['bear', 'man', 'pig']
"""

animals = ['man', 'bear', 'pig']
more_animals = ['cow', 'duck', 'horse']
all_animals = animals + more_animals
print(all_animals)

#['man', 'bear', 'pig', 'cow', 'duck', 'horse']

animals = ['man', 'bear', 'pig']
print(len(animals))
animals.append('cow')
print(len(animals))

#3
#4


#Ranges
for number in range(3):
	print(number)
#0
#1
#2

for number in range(1,3):
	print(number)
#1
#2

for number in range(1, 10, 2):
	print(number)
#1
#3
#5
#7
#9

animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse', 'dog']
for number in range(0, len(animals), 2):
	print(animals[number])

"""
man
pig
duck
dog
"""





























