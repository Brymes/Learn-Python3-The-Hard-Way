from sys import exit

class Garage():
    
    def enter(self):
        print('''
There happens to be a Motor Park in front of you.
You walk inside...It's more or less empty.
Now to find the perfect place to sleep.''')
        print('_' * 35)
        print('Where do you Sleep?')
        print('''
1. An empty bus.
2. On a  mat under a shed
''')

        choice = input('Enter your choice >> ')

        if choice == '1':
                print('''
So you walk up to the empty bus...You open the door...
Walk up to the last row... lay down and sleep...
Meanwhile in your sleep.....Some guys came there to steal...
And there's a bag filled with valuables in the bus(The target of the thieves)
Now they take the bag, and also steal your phone.
In the Morning.... you are woken up by the Driver who belwives you were the bandit
You try to explain...But he ends up stabbing you and tossing your corpse into a canal.
''')
                exit()
        elif choice == '2':
                print('''You sleep on a mat under a shed..In your sleep
A scorpion gent;y crawls up on your body then to your chest...
You wake up and try to move..Then it stings you sirectly in the chest.''')
                exit()

