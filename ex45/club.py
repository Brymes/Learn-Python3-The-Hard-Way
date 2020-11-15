from sys import exit

class Club():
    def enter(self):
        print('''
So you enter the nearest clubhouse to you....
You look around...The perfect place.
Now you have choices.
Do you?
1. Sleep in their Staff mess room.
2. Blend in Have some drinks. And Party
''')
        
        choice = input('Enter your choice >> ')
        
        if choice == '1': 
            return Club().Sleep()
        elif choice == '2':
            return Club().Party()
        else:
            print('Sorry i didn\'t get that.')
    
    
    def Sleep(self):
        print('_' * 35)
        print(''' 
You have access to a staff mess room where you lay your head to sleep.
Well as you sleep. A staff finds it nice to commit a crime of stealing and leave you hanging.
You end up with 3 nights in the station before you were able to clear your name.''')
        exit()

    def Party(self):
        print('_' * 35)
        print('''
You buy yourself some drinks...You start to dance....
A couple of more shots and you're starting to get drunk
In the process you start to dance with the girl of this drug dealer.
Now He gets angry...And shoots you on the spot...
...The rest is History''')
        exit()

        
