# The "end=' '" makes the prompt answer on the line instead of new line
print('How old are you?', end=' ')
age = input()
print('How tall are you?', end=' ')
height = input()
print('How much do you weigh?', end=' ')
weight = input()

print(f"So you're {age} years old, {height} tall and {weight} heavy.")
