states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California ': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Fransisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print('Michigan\'s abbreviaiton is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

print('-' * 10)
print('Michcigan has: ', cities['MI'])
print('Florida has: ', cities ['FL'])

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(states.items()):
	print(f'{abbrev} has the city {city}')

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbbreviated {abbrev}")
	print(f'and has city {cities[abbrev]}')

print('-' * 10)
state = states.get('Texas')

if not state:
	print('Sorry, no Texas.')

#get a city with a default value?
city = cities.get('TX', 'Does Not Exist')
print(f'The city for the state \'TX\' is: {city}')	


