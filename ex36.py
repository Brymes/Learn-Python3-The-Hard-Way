from sys import exit

def dead(why):
	print(why, ', Game over.')
	exit(0)

def cbn():
	print('You\'re in the vault of the Central Bank.')
	print('How much do you take?')

	choice = int(input('>> #'))

	if choice < 10000000:
		dead('Good job!')
	elif choice > 10000000:
		dead('you\'re quite greedy.')
	elif choice == 10000000:
		dead('You\'re moderate in your choices.')
def bear_room():
	print('There are 2 bears here And a pot of honey with a gun on a table.')
	print('How do you escape?')
	print('1. Take the gun and shoot the bears.')
	print('2. Throw the pot of honey out of the window.')

	choice = input('>> ')

	if choice == '1':
		dead('The bear gets upset and eats your face off')
	elif choice == '2':
		print('Smart choice the bear jumps out following the honey.')
		print('Here\'s your reward')
		cbn()
	else:
		print('No response from you.')
		dead('The Bears tear you apart.')

def pyramid():
	print('You find yourself inside a pyramid full of gold.')
	print('Do you?')
	print('1. Start taking the gold.')
	print('2. Find your way out.')
	print('3. Take a bit then find your way out.')

	choice = input('>> ')

	if choice == '1':
		dead('The entire pyramid falls and crashes on you.')
	elif choice == '2':
		print('Smart choice, You found your way out. Here\'s your reward.')
		cbn()
	elif choice == '3':
		print('Smart choice, Now you\'are not only richer by a few gold, The police are after you.')
		dead('Good job.')
	else:
		print('I have no idea what that is.')
		pyramid()

def start():
	print('You wake up in the middle of the night and see 2 doors.')
	print('Pick a number')
	print('1. Door 1')
	print('2. Door 2')
	print('3. Sleep back')
	
	choice = input('>> ')
	
	if choice == '1':
		bear_room()
	elif choice == '2':
		pyramid()
	elif choice == '3':
		print('Hurray you found the Easter Egg.')
		cbn() 
	else:
		print('Enter number OR type sleep')
		start()

start()
