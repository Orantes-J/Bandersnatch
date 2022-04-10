# IMPORTS / MODULES
from helper import astrid, emotions_list

# PATH 1 MODULE
from path1 import a, b

STATE = True
# OPEN TXT FILE WITH ASCII ART
with open('ascii.txt', 'r') as file:
    print(''.join([line for line in file]))

astrid()
user_name = input('What is your first name? ')
first_response = input(f'\nHow is your day {user_name}? ')

for i in emotions_list:
    if first_response == i:
        a = a(first_response)
        print(f'{a} {user_name}.')
        b()
        print('\nAhh interesting!')
        user_input_1 = input('\nWhat about a favorite movie? ')
        input(f'\nWhy do you like {user_input_1}? ')

else:
    print('condition was not met')
print('*'*60)