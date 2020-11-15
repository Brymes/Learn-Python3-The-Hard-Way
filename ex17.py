from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}" + '\n')

From = open(from_file).read()

print(f"The input file is {len(From)} bytes long")
{exists(to_file)}
print("Ready, hit RETURN to copy")
print('If not CTRL-C to abort.')
input()

To =open(to_file, 'w').write(From)


print('Alright, all done.')
