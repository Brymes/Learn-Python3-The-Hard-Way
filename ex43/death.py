from sys import exit
from scene import Scene

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
