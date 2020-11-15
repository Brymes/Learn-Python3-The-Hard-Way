from scene import Scene
from random import randrange

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
                
