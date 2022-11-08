import os
import webbrowser
import speech_recognition
import pyttsx3
import tkinter as tk

from random import choice
from serpapi import GoogleSearch
from tkinter.filedialog import askdirectory

# объект для прослушивания

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
sr.energy_threshold = 400

list_commands = {
    'commands': {
        'greeting': ['привет', 'Максон', 'привет максон', 'эй максон'],
        'create_todo_list': ['добавить задачу'],
        'view_todo_list': ['посмотреть список дел', 'открой список дел'],
        'play_sound': ['включи музыку'],
        'open_browser': ['открой браузер'],
        'internet_search': ['поиск', 'найди'],
        'shutdown_reboot_pc': {
            'shutdown_reboot_pc': ['выключи', 'перезагрузи', 'выруби', 'отключи', 'перезагрузка', 'ребут']
        },
        'open_internet_search': ['открой', 'перейди', 'покажи']
    },
    'directory': '0'
}

# функция прослушивания микрофона


def listen_command():
    with speech_recognition.Microphone() as micro:
        sr.adjust_for_ambient_noise(source=micro, duration=0.5)
        print('Можно говорить')
        try:
            audio = sr.listen(source=micro)
            phrase = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            print(phrase)
            return phrase
        except speech_recognition.UnknownValueError:
            print('Ошибка, повторите фразу')
            listen_command()


def answer_function(text: str):
    answer = pyttsx3.init()
    answer.say(text)
    answer.runAndWait()
    answer.stop()


def greeting():
    answer_function('Приветствую, что хотели?')
    return 'Приветствую, что хотели?'


def shutdown_reboot_pc(value: str):
    lst = value.split()
    commander_s = ['выключи', 'выруби', 'отключи']
    commander_r = ['перезагрузка', 'перезагрузи', 'ребут']
    if any(x in lst for x in commander_s):
        answer_function('Выключение через 3 секунды')
        os.system('shutdown /s /t 3')
    if any(x in lst for x in commander_r):
        answer_function('Перезагрузка через 3 секунды')
        os.system('shutdown /r /t 3')


def open_browser():
    files = r'C:\Program Files (x86)\Yandex\YandexBrowser\Application\browser.exe'
    os.startfile(files)


def create_todo_list():
    answer_function('Что добавим в список дел?')
    phrase = listen_command()
    if os.path.exists('To_Do_list.txt'):
        x = 'a'
    else:
        x = 'w'
    with open('To_Do_list.txt', x) as file:
        file.write(f'{phrase}\n')
    answer_function(f'Задача {phrase} записана в список дел')


def view_todo_list():
    with open('To_Do_list.txt') as file:
        for line in file:
            print(line)


def play_sound():
    if list_commands['directory'] == '0':
        window = tk.Tk()
        intro = tk.Label(text="Выберите папку с музыкой\n(для продолжения закройте это окно)",
                         width=40, height=4, font='Times 20')
        intro.pack()
        window.mainloop()
        folderlocation = askdirectory()
        list_commands['directory'] = folderlocation

    files = os.listdir(list_commands['directory'])
    if len(files) != 0:
        random_file = f'{choice(files)}'
        answer_function(f'Колбасимся под {random_file.split("/")[-1]}')
        os.startfile(fr"C:\Users\Максим\Desktop\Music\{random_file}")
        return f'Слушаем {random_file.split("/")[-1]}'
    else:
        answer_function('Музыки по адресу нет')
        return 'Музыки по адресу нет'


def internet_search():
    answer_function('Что хотите найти?')
    phrase = listen_command()
    parameter = {
        "engine": "yandex",
        "text": phrase,
        "api_key": "1a15ef08c83fb7bba62201558cd28c125d1eccab2a77a808e84ed7aa55f20d3f"
    }

    search = GoogleSearch(parameter)
    dict_results = search.get_dict()

    print(dict_results['organic_results'][0]['link'])
    print(dict_results['organic_results'][0]['snippet'])
    answer_function(dict_results['organic_results'][0]['snippet'])


def open_internet_search():
    answer_function('Какую ссылку открыть?')
    phrase = listen_command()
    parameter = {
        "engine": "yandex",
        "text": phrase,
        "api_key": "1a15ef08c83fb7bba62201558cd28c125d1eccab2a77a808e84ed7aa55f20d3f"
    }

    search = GoogleSearch(parameter)
    dict_results = search.get_dict()
    webbrowser.register('YandexBrowser', None,
                        webbrowser.BackgroundBrowser(
                            r'C:\Program Files (x86)\Yandex\YandexBrowser\Application\browser.exe'))
    webbrowser.get('YandexBrowser').open_new_tab(dict_results['organic_results'][0]['link'])


def main():
    print('start')
    n = 0
    while True:
        n += 1
        print(f'цикл {n}')
        phrase = listen_command()

        for key, value in list_commands['commands'].items():
            if phrase in value:
                print(phrase)
                print(globals()[key]())
                continue
            else:
                if type(list_commands['commands'][key]) is dict:
                    for key_c, value_c in list_commands['commands'][key].items():
                        if phrase in value_c:
                            print(globals()[key_c](phrase))
                            continue
                        else:
                            print('Повтори фразу')
                            continue
