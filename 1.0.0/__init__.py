import os
import json
import time
import random
import datetime
import configparser
from lists import *

__author__ = 'Elisei Sharov'

VERSION = '1.0.0'

achievements = []

date = datetime.datetime.now()

with open('config.json', mode='r') as f:
    data = json.load(f)
    choosen_lang = data['language']
    if choosen_lang == 'Russian':
        lang = 'ru'
    elif choosen_lang == 'English':
        lang = 'en'
    elif choosen_lang == 'Japanese':
        lang = 'jp'
    else:
        print('Language is not finded. Please, check value in key "language" in file "config.json"')
        time.sleep(5)
        os.startfile('config.json')

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

class Main(object):
    def __init__(self, settings=['en', 'saved_game_1']):
        self.language = settings[0]
        self.load_game = settings[1]

load = '1'
game = Main(settings=[lang, load])

def log(text):
    with open('log.txt', mode='a') as f:
        f.write('\n[{}]: {};'.format(date, text))

def menu():
    log('The menu() function is called')
    n = 0
    try:
        while True:
            if game.language == 'ru':
                print(start_menu_ru[n])
            elif game.language == 'en':
                print(start_menu_en[n])
            elif game.language == 'jp':
                print(start_menu_jp[n])
            n += 1
    except:
        pass

def ghelp():
    log('The ghelp() function is called')
    n = 0
    try:
        while True:
            if game.language == 'ru':
                print(helping_info_ru[n])
            elif game.language == 'en':
                print(helping_info_en[n])
            elif game.language == 'jp':
                print(helping_info_jp[n])
            n += 1
    except:
        pass

def game_info():
    n = 0
    try:
        while True:
            if game.language == 'ru':
                print(game.game_info_ru[n])
            elif game.language == 'en':
                print(game.game_info_en[n])
            elif game.language == 'jp':
                print(game.game_info_jp[n])
    except:
        pass

def authors():
    n = 0
    try:
        while True:
            if game.language == 'ru':
                print(game.authors_ru[n])
            elif game.language == 'en':
                print(game.authors_en[n])
            elif game.language == 'jp':
                print(game.authors_jp[n])
    except:
        pass

def exit():
    log('The exit() function is called')
    quit()

if game.language == 'ru':
    log('Runned Russian launcher')
elif game.language == 'en':
    log('Runned English launcher')
elif game.language == 'jp':
    log('Runned Japanese launcher')

save_id = 0

def new_game():
    log('Started new game')
    if game.language == 'ru':
        print(game_guide_ru[0])
        nickname = input('Введи свой ник: ')
        password = input('Теперь, придумай пароль: ')
        print(game_guide_ru[1])
        command = input('$login - ')
        if command == 'server:skip':
            print(game_guide_ru[2])
            achievements.append('Неплохо, для начала')
        elif command == 'アニメ:らき☆すた':
            log('Anime-achievement was given to {}'.format(nickname))
            achievements.append('Анимешник')
            print(game_guide_ru[4])
            with open('save_{}.json'.format(save_id), mode='w') as f:
                dict = {}
                dict['nick'] = 'kagamine'
                dict['pass'] = 'iwantto_withkonata'
                json.dump(dict, f)
        elif command == '{}:{}'.format(nickname, password):
            print(game_guide_ru[3])
            achievements.append('Глупец')
            with open('save_{}.json'.format(save_id), mode='w') as f:
                dict = {}
                dict['nick'] = nickname
                dict['pass'] = password
                json.dump(dict, f)
        else:
            print('Попробуй снова')
            new_game()


class Chapter1:
    def __init__(self, started=False):
        self.started = started

class Chapter2:
    def __init__(self, started=False):
        self.started = started

class Chapter3:
    def __init__(self, started=False):
        self.started = started

class Chapter4:
    def __init__(self, started=False):
        self.started = started