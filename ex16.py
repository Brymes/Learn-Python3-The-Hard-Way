from sys import argv

script, filename = argv

print(f"We're going to  erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print('If you do wnat that, hit RETURN')

input('?')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
target.truncate

print("Now I'm going to ask you for three lines.")

line1 = input('line1:')
line2 = input('Line2:')
line3 = input('line3:')

print("I'm going ot write these to the file.")

target.write(line1 +'\n' +line2 +'\n' +line3 )

print("And finally, we close it.")
target.close()


#read file we just wrote to
txt = open(filename)
txt.seek(0)
print('\n')
print(txt.read())
