from random import randrange
from sys import exit

def play():
	print('Welcome to your game of guess the pin')
	pin_right = False
	
	while True:
		pin1 = print('1.' + str(randrange(1000, 9999)))
		pin2 = print('2.' + str(randrange(1000, 9999)))
		pin3 = print('3.' + str(randrange(1000, 9999)))
		

		choice = input('>> ')
		if choice == '1':
			print('Wrong. You have another chance')
			pin_right = False
		
		elif choice == '2':
			print('Correct choice you move on.')
			pin_right = True
			exit()
		
		elif choice == '3':
			print('Wrong you have another chance')
			pin_right = False
		
		else:
			print('Sorry didn\'t get that')
			pin_right = False
play()
