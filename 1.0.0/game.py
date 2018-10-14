from __init__ import *

__author__  = 'Elisei Sharov'

menu()

while True:
    a = input('$ ')
    if a == 'menu':
        menu()
    elif a == 'ghelp':
        ghelp()
    elif a == 'new_game':
        new_game()
    elif a == 'exit':
        exit()
    else:
        print('Command isn\'t finded')
        log('Called unknown command "{}"'.format(a))