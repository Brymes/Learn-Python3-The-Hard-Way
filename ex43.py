from sys import exit
from random import randrange

class Scene(object):
    
    def enter(self):
        print('This scene is not yet configured.')
        print('Subclass it and implement enter().')
        exit(1)


class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()



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


class TheBridge(Scene):

    def enter(self):
        print('_' * 30)
        print('''Now you're at the bridge.
Here you find another gothon,
Your only obstacle to planting the bomb.''')
        print('_' * 30)
        print('''There are 2 items on the floor next to you..
        1. A Human Brain
        2. A Space Rocket Launcher''')
        print('_' * 30)
        print('What do you do?')
        print('_' * 30)
        print('''Do you:
        1. Throw the brain at the Gothon.
        2. Shoot a rocket at the Gothon.''')
        
        choice = input('>> ')
        
        if choice == '1':
            print('Smart choice')
            return'escape_pod'
        elif choice == '2':
            death.Death2('In shooting you accidentaly activate the bomb.')


class EscapePod(Scene):   
    
      def enter(self):
        print('_' * 30)
        print('You have made it to the end of the game now you have to escape.')
        print('Pick the right escape pod.')
        
        pin_right = False
        
        print('_' * 30)
        while True:
            pod1 = print('Pod1. ' + str(randrange(1,50)))
            pod2 = print('Pod2. ' + str(randrange(1,50)))
            pod3 = print('Pod3. ' + str(randrange(1,50)))
            pod4 = print('Pod4. ' + str(randrange(1,50)))
            pod5 = print('Pod5. ' + str(randrange(1,50)))
            pod6 = print('Pod6. ' + str(randrange(1,50)))
            pod7 = print('Pod7. ' + str(randrange(1,50)))
            
            choice = input('>> ')
            
            W = ['1', '2', '3', '5', '7']
            R = ['4', '6']
           
            if choice in W:
                print('Wrong pod')
                pin_right = False
            elif choice in R:
                print('Correct pod')
                return 'finished'
            else:
                print('Sorry didn\'t get that')
                

        
                

class Death(Scene):
    
    def Death1(self, why):
        print('Wrong choice.')
        print(why)
        print('The Gothon then abducts you and melts your brain.')
        print('Game Over.')
        exit()
    
    def Death2(self, why):
        print('Wrong choice.')
        print(why)
        print('You blow up yourself and the gothon to pieces.')
        print('Game Over.')
        exit()


class Finished(Scene):
    
    def enter(self):
        print('You won! Good job.')
        return 'finished'


class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
        }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
