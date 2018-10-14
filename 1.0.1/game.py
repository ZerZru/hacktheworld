from __init__ import *

__author__  = 'Elisei Sharov'

menu()

while True:
    a = input('$ ')
    if a == functions[0]:
        menu()
    elif a == functions[1]:
        load_game()
    elif a == functions[2]:
        ghelp()
    elif a == functions[3]:
        exit()
    elif a == functions[4]:
    	new_game()
    else:
        print('Команда не найдена')