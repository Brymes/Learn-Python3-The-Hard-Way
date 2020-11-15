#It's meant to be argv + input/// but idk wtf this is 
from sys import argv
First = input('1st variable? ')
Second = input('2nd variable? ')
Third = input('3rd variable? ')
Fourth = input('4th variable? ')

script, First, Second, Third, Fourth = argv

print('the script is called:', script)
print('your first variable is:', First)
print('your second variable is:', Second)
print('your third variable is:', Third)
print('your Fourth variable is:', Fourth)
