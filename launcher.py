#importing packages
import os
import json
import shutil
import random
from tkinter import *

#app's lists
errors = [
    'in file "config.json" key "language" have incorrect value.\n This key can contain only "Russian", "English" and "Japanese" values',
    'you choose an unknown(or incorrect wroted) version.\n Please, check value of key "current_version"'
]

versions = [
    '1.0.0',
    '1.0.1'
]

news_ru = [
    'Первая версия HackTheWorld была создана\n4/8/2018, но выпущена 20/10/2018',
    'Что такое Project SC? Никто не может знать',
    'Также попробуйте HackingSim от DevFoxGames!',
    'SCG вернулась в разработку игр',
    'Сможете ли вы найти все пасхалки в игре?\nПосмотрим, посмотрим...'
]

news_en = [
    'First version of HackTheWorld was created\nat 8/4/2018, but published at 20/10/2018',
    'What is Project SC? Nobody can not know',
    'Also try HackingSim from DevFoxGames!',
    'SCG come back to game developing',
    'Can you find all easter eggs in game?\nWill see, will see...'
]

news_jp = [
    'First version of HackTheWorld was created\nat 4/8/2018, but published at 20/10/2018',
    'What is Project SC? Nobody can not know',
    'Also try HackingSim from DevFoxGames!',
    'SCG come back to game developing',
    'Сможете ли вы найти все пасхалки в игре? Посмотрим, посмотрим...'
]

#app
root = Tk()
root.title('HackTheWorld')
root.geometry('500x500')

#config reading
with open('config.json', mode='r') as f:
    data = json.load(f)
    language = data['language']
    last_version = data['last_version']
    current_version = data['current_version']
    versions_count = int(data['versions_count'])

#app's main functions
def start_game():
    shutil.copyfile(r'config.json', r'{}\config.json'.format(current_version))
    os.startfile(r'{}\game.py'.format(current_version))

def download(version):
    #code
    pass

def oppen():
    os.startfile('config.json')

    error_id = int(error_id)
    root.title('HackTheWorld: ' + error_name)
    text = Label(text="Detected {}.\nIt's means, what {}".format(error_name, errors[error_id]))
    button = Button(text='Open file "config.json"', command=oppen)
    text.place(x=0, y=0)
    button.place(x=140, y=60)
    root.mainloop()

#russian language
def Rlauncher():
    random_news = Label(text=random.choice(news_ru))
    version_text = Label(text='Загрузить: HackTheWorld - версия {}'.format(current_version))
    play_button = Button(root, text='Запустить игру', width='30', height='2', command=start_game)
    random_news.place(x=130, y=0)
    version_text.place(x=130, y=420)
    play_button.place(x=130, y=450)
    root.mainloop()

#english language
def Elauncher():
    random_news = Label(text=random.choice(news_en))
    version_text = Label(text='Load: HackTheWorld - version {}'.format(current_version))
    play_button = Button(root, text='Launch game', width='30', height='2', command=start_game)
    random_news.place(x=130, y=0)
    version_text.place(x=130, y=420)
    play_button.place(x=130, y=450)
    root.mainloop()

#japanese language
def Jlanguage():
    random_news = Label(text=random.choice(news_jp))
    version_text = Label(text='ダウンロード: HackTheWorld - バージョン {}'.format(current_version))
    play_button = Button(root, text='ゲームを實子する', width='30', height='2', command=start_game)
    random_news.place(x=130, y=0)
    version_text.place(x=110, y=420)
    play_button.place(x=130, y=450)
    root.mainloop()

num = 0
while True:
    if num > versions_count:
        errors_window('VersionError', 1)
        break
    else:
        if current_version == versions[num]:
            if language == 'Russian':
                Rlauncher()
            elif language == 'English':
                Elauncher()
            elif language == 'Japanese':
                Jlanguage()
            else:
                errors_window('LanguageError', 0)
            break
        else:
            num += 1