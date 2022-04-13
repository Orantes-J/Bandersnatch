from helper import indent

def a1(att):
    return f"I'm sorry you are having a {att} day "

def a2():
    user_input = input('Can I cheer you up with a game, it will distract you from reality?(yes/no) ')
    indent()
    if user_input.lower() != 'yes':
        with open('src/asciiGOver.txt', 'r') as file:
            print(''.join([line for line in file]))
        return False
    else: 
        return 'Great let us get started!'