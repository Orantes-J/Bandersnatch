from helper import *

#PATH 2 STORY CHARACTERS 
mc = 'Sasuke'
scn = 'Naruto'
scs = 'Sakura'

def a1(att):
    return f"I'm sorry you are having a {att} day "

def a2():
    user_input = input('Can I cheer you up with a game, it will distract you from reality?(yes/no) ')
    indent()
    if user_input.lower() != 'yes':
        game_over()
        return False
    else: 
        return 'Great let us get started!'

def enter_sasuke():
    print(f"My name is {mc} Uchiha..\nI don't like many things\nAs the lone Uchiha, I only have one dream and I will make into a reality...")
    indent()
    print(f'{n}A few days have passed and {mc} comes across {scn} at the near by hangout spot with {scs}')

def greet_naruto():
    greeted = input(f'{scn} is so annoying. Here he comes ~ Should I say hi? (yes/no)')

    if greeted == "yes":
        print(f'{n}And so {mc} greeted {scn}, {scn} was confused by this but still greeted back')
    
    if greeted == "no":
        print(f'{n}And {mc} ignored {scn}, but we all know how Naruto is.')