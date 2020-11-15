from scene import Scene

class CentralCorridor(Scene):
 
    def enter(self):
        print('''Aliens have invaded your space ship, 
You have to go through a maze of rooms defeating them
Your escape will be through an escape pod before you destroy the ship.
Good Luck
Welcome to Space Hero.''')
        print('_' * 30)
        print('You\'re at the central corridor and you have an Aichmophobic gothon in front of you')
        print('''There are 4 items on the floor beside you.
        1.A Needle
        2.A rail gun 
        3.An Axe
        4.A flame thrower
        5.A grenade''')
        print('_' * 30)
        print('What do you do?')
        print('_' * 30)
        print('''Do you:
        1. Use the needle to scare the Gothon. 
        2. Shoot the Gothon with the rail gun.
        3. Attack the Gothon with the axe.
        4. Use the flame thrower on the Gothon.
        5. Use the grenade.''')
        
        choice = input('>> ')
                
        if choice == '2' or choice == '3':
            Death().Death1('The gothon gets upset and slaps the weapon out of your hand.')
        elif choice == '4' or choice == '5':
            Death().Death2('Gothon blood is flammable.')
        elif choice == '1':
            print('smart choice.')
            return 'laser_weapon_armory'
        else:
            print('Sorry, I didn\'t get that.')
