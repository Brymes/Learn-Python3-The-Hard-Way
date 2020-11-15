from scene import Scene
from random import randrange

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print('_' * 30)
        print('Welcome to the Laser Weapon Armory.')
        print('Input the right pin into the keypad to get a neutron bomb.')
        pin_right = False
	
        print('_' * 30)
        while True:
            pin1 = print('1.' + str(randrange(1000, 9999)))
            pin2 = print('2.' + str(randrange(1000, 9999)))
            pin3 = print('3.' + str(randrange(1000, 9999)))
		

            choice = input('>> ')
            if choice == '1':
                print('Wrong. You have another chance')
                pin_right = False
		
            elif choice == '2':
                print('Pin correct.Take your neutron Bomb.')
                pin_right = True
                return 'the_bridge'
           
            elif choice == '3':
                print('Wrong you have another chance')
                pin_right = False
		
            else:
                print('Sorry didn\'t get that')
                pin_right = False
