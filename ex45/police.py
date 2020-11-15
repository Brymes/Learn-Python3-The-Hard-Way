from sys import exit

class PoliceStation():
    
    def enter(self):
        print('''
So you walk into the nearest Police station.
You were offered a place to sit...Well not much of a bed.
But you could at least do a nap on your neck.
Well you think all is well until you're woken up with the butt of a gun.
Apparently someone reported a crime. And they caught the culprit.
The culprit bribed his way through. And as the case had already been documented.
They needed another person to take the fall...And you walked in there as a suitable candidate
You were charged to court the next Monday.
You were asked Guilty or not Guilty to the crime.
The Police had a proposal to you in which you plead guilty..And then after sentencing you..They find a way to bring you out.
''')
        print('_' * 35)
        print('What do you do?')
        print('''
Do you?
1. Plead Guilty
2.Plead not Guilty.
''')

        choice = input('Enter your choice >> ')

        if choice == '1':
            print('Well you believe all things go according to plan until You get shot while in transit to prisonand you die')
            exit()
        elif choice == '2':
            print('Good choice...you were later on vindicated as a result of lack of sufficient evidence.')
            exit()
        else:
            print('Sorry i didn\'t get that')

