"""
Hold key-value pairs called items
AKA associative arrays, hash tables and hashes

dictionary_name = {key_1: value_1, key_N: value_N}
dictionary_name = {}
dictionary_name[key]

"""
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
jasons_phone = contacts['Jason']
carls_phone = contacts['Carl'] 

print('Dial {} to call Jason.'.format(jasons_phone))
print('Dial {} to call Carls.'.format(carls_phone))

contacts = {'Jason': '555-0123', 'Carl':'555-0987'}
contacts['Jason'] = '555-0000'
jasons_phone = contacts['Jason']
print('Dial {} to call Jason.'.format(jasons_phone))

contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
contacts['Tony'] = '555-0570'
print(contacts)
print(len(contacts))

contacts = {'Jason': '555-0123', 'Carl':'555-0987'}
del contacts['Jason']
print(contacts)

contacts = {
	'Jason': ['555-0123', '555-0000'],
	'Carl': '555-0987'
}
print('Jason:')
print(contacts['Jason'])
print('Carl:')
print(contacts['Carl'])

contacts = {
	'Jason': ['555-0123', '555-0000'],
	'Carl': '555-0987'
}

for number in contacts['Jason']:
	print('Phone: {}'.format(number))

contacts = {
	'Jason': ['555-0123', '555-0000'],
	'Carl': '555-0987'
}

if 'Jason' in contacts.keys():
	print("Jason's phone number is:")
	print(contacts['Jason'][0])

if 'Tony' in contacts.keys():
	print("Tony's phone number is:")
	print(contacts['Tony'][0])

"""
Jason's phone number is:
555-0123

"""

contacts = {
	'Jason': ['555-0123', '555-0000'],
	'Carl': '555-0987'
}

print('555-0987' in contacts.values())
#True

"""
Loops 
for key_variable in dictionary_name:
	#Code block
	#dictionary_name[key_variable]

for conttact in contacts:
	#Code block
for person in people
	#Code block
"""

contacts = {
	'Jason': '555-0123',
	'Carl': '555-0987'
}


for contact in contacts:
	print('The number for {0} is {1}.'.
		format(contact, contacts[contact]))

"""
The number for Jason is 555-0123.
The number for Carl is 555-0987.
"""






































