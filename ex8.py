formatter='{} {} {} {}'

print(formatter.format(1,2,3,4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	'Life could be',
	'Somewhat shitty at times',
	'But just keep moving',
	'Like what else do we have'
))
