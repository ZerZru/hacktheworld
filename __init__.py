import os
import json
import time
import random
import configparser

__author__ = 'Elisei Sharov';

VERSION = '1.0.0'

#lists

functions = [
    'menu',
    'load_game',
    'ghelp',
    'exit',
    'new_game',
    'game_info',
    'authors',
    'save_game'
]

start_menu = [
    'Новая игра - new_game\n',
    'Загрузить игру - load_game\n',
    'Помощь - ghelp\n',
    'Выход - exit\n'
]

helping_info = [
      'Добро пожаловать в HackTheWorld: гайды\n',
      'Здесь вы можете получить любую интересующую вас информацию\n',
      'Чтобы получить информацию о функции, игре или авторстве программы,'
    + 'введите название функции, game_info или authors\n'
]

#defining functions

def menu(): #function menu, 
    print(start_menu[0], start_menu[1], start_menu[2], start_menu[3])

def new_game():
    user = input('Пожалуйста, введите своё имя: ')
    passw = input('Придумайте пароль для игры: ')

    with open('saves.json', mode='r') as f:
        data = json.load(f)
        games_count = data['count']

    with open('saved_games.ini', mode='a') as f:
        f.write('\n\n[game_{}]\nuser={}\npassw={}'.format(games_count, user, passw))
        ACTIVATED_GAME = games_count

    with open('saves.json', mode='w') as f:
        dict = {}
        dict['count'] = games_count + 1
        json.dump(dict, f)

def load_game():
    a = input('Пожалуйста, введите ID сохранения, которую вы хотите загрузить: ')

def ghelp():
    print(helping_info[0], helping_info[1], helping_info[2])

#def save_game():


def exit():
    quit()