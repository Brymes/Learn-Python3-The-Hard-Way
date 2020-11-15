class IkejaUnderBridge():
    def enter(self):
        print('''
You're stranded on a Firday night at Ikeja at 11:30 pm ....
You have a few options
---------------------------------------------
Do you 
1. Go to the nearset police station.
2. Find a Church or Mosque.
3. Find the nearest Bar or Club-house
4. Sleep at the nearest garage
''')
        print('_' * 35)
        choice = input('Enter the number of your choice >>  ')
        print('_' * 35)

        if choice == '1':
            return 'police'
        elif choice == '2':
            return 'religion'
        elif choice == '3':
            return 'club'
        elif choice == '4':
            return 'garage'
        else:
            print('Sorry i didn\'t get that')
