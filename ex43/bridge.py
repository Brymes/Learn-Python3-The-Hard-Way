from scene import Scene

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
