# PY IMPORTS/MODULES
from distutils.log import error
import sys

# HELPER MODULE
from helper import *

# PATH 1 MODULE
from path1 import *
from path2 import *

game_state = True
# OPEN TXT FILE WITH ASCII ART
welcome_user()
indent()

user_name = input('What is your first name? ')

def ask_abt_day():
    i = input(f'\nHow is your day {user_name}? ')
    if i != 'yes' or 'no':
        raise error
    return i

first_response = ask_abt_day()

while True:
    # PATH 1 SET CHARACTER AS NARUTO POV
    for i in good_vibes:
        if first_response == i:
            a = a(first_response)
            print(f'{a} {user_name}.')

            res = b()
            if res == False:
                game_state = False

            # GUARD CLAUSE
            if first_response != i:
                pass

    # PATH 2 SET CHARACTER AS SASUKE POV
    for i in bad_vibes:
        if first_response == i:
            f_reply = a1(first_response)
            indent()
            print(f'{f_reply}{user_name} ):')
            indent()

            # THIS BLOCK WILL DETERMINE GAME START OR GAME OVER 
            res = a2()
            if res == False:
                game_state = False

            # BLOCK IS FIRST CHOICE (GREET NARUTO)
            enter_sasuke()
            indent()
            greet_naruto()

    if game_state != True:
        indent()
        sys.exit("- Hint: 'Choose a different path'")

