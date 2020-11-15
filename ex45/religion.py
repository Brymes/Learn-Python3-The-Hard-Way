from sys import exit

class ReligiousPlace():
    
    def enter(self):
        print('''
So you walk into the nearest place of Worship.
You see the cleric in charge and narrate your ordeal
He ponders for a minute and allows you to stay...
.................................................
Now the pastor's son sees a chance to commit a crime of robbing the vestry..
He calls in the robbers and they perpetrate the act.
In the process you were awoken by their noise...
Now what do you do?''')
        
        print('_' * 35)
        print('Do you?')
        print('''
1. Call the police in.
2. Run away.
''')

        choice = input('Enter your choice >> ')

        if choice == '1':
            print('_' * 35)
            print('''
The Logical and Smart choice.
But well it turns out the police are also involved in their shit.
Well you get dragged into it and get ultimately framed.
Leading you to a jail term of 1 year.
''')
        elif choice == '2':
            print('_' * 35)
            print('''
Well it's almost morning.So you pick yourself up and run.
You end up in your house safe and unharmed.
''')
        print('_' * 35)
        print('''
Congratulations Gladiator.You made it to the end
Game over''')
        exit()

