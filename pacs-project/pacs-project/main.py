# PY IMPORTS/MODULES
import sys

# HELPER MODULE
from helper import astrid, good_vibes, bad_vibes, indent

# PATH 1 MODULE
from path1 import a, b
from path2 import a1, a2

game_state = True
# OPEN TXT FILE WITH ASCII ART
with open('src/asciiWelcome.txt', 'r') as file:
    print(''.join([line for line in file]))

astrid()
user_name = input('What is your first name? ')
first_response = input(f'\nHow is your day {user_name}? ')

while True:
    # PATH 1
    for i in good_vibes:
        if first_response == i:
            a = a(first_response)
            print(f'{a} {user_name}.')
            b()
            indent()
            print('Ahh interesting!')
            user_input_1 = input('\nWhat about a favorite movie? ')
            indent()
            input(f'Why do you like {user_input_1}? ')
    
    # PATH 2
    for i in bad_vibes:
        if first_response == i:
            f_reply = a1(first_response)
            indent()
            print(f'{f_reply}{user_name} ):')
            indent()
            res = a2()
            if res == None or res == False:
                game_state = False
            if res:
                print(res)
                astrid()

    if game_state != True:
        indent()
        sys.exit("- Hint: 'Choose a different path'")

