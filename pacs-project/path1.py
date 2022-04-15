from helper import *

#PATH 1 STORY CHARACTERS 
mc = 'Naruto'
scs = 'Sasuke'
scsa = 'Sakura'
me = 'Juan'

def a(att):
    return f'\nI am glad you are having a {att} day'

def b():
    user_input = input('\nI have an idea let us a play a game?(yes/no) ')

    if user_input == 'yes':
        print('Great let us get started!\n')
        game_start()
    else:
        game_over()
        return False

def enter_naruto():
    print(f'I am {mc} Uzumaki, and I want to be Hokage.\nSo everybody can stop disrespecting me and they will have to look up to me, BELIEVE IT!!')

def greet_sasuke():
    greeted = input(f"Look at {scs}, he always thinks he soo cool. I don't even want to say hi ~ Should I say hi? (yes/no)")

    if greeted == 'yes':
        print(f'{n}And so {mc} put his wants to the side and only said hi.')
    
    if greeted == 'no':
        print(f"{n}So")