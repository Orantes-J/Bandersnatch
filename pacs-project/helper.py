n = 'Narrator : '

def astrid():
    print('*'*116)
def indent():
    print('\n')

def welcome_user():
    with open('src/asciiWelcome.txt', 'r') as file:
        print(''.join([line for line in file]))
def game_start():
    with open('src/asciiGStart.txt', 'r') as file:
        print(''.join([line for line in file]))
def game_over():
    with open('src/asciiGOver.txt', 'r') as file:
        print(''.join([line for line in file]))

good_vibes = ['good', 'alright', 'chill', 'decent']
bad_vibes = ['complicated', 'dumb', 'stressful', 'overwhelming', 'bad']