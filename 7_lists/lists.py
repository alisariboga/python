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





























