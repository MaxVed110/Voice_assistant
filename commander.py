import os
import speech_recognition
import pyttsx3
from random import choice

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

list_commands = {
    'commands': {
        'greeting': ['привет'],
        'create_todo_list': ['добавить задачу'],
        'play_sound': ['включи музыку'],
        'open_browser': ['открой браузер'],
        'shutdown_reboot_pc': {
            'shutdown_reboot_pc': ['выключи', 'перезагрузи']
        }
    }
}


def listen_command():
    with speech_recognition.Microphone() as micro:
        sr.adjust_for_ambient_noise(source=micro, duration=0.5)
        try:
            audio = sr.listen(source=micro)
            phrase = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return phrase
        except speech_recognition.UnknownValueError():
            print('Повтори фразу')


def answer_function(text: str):
    answer = pyttsx3.init()
    answer.say(text)
    answer.runAndWait()
    answer.stop()


def greeting():
    answer_function('Приветик')
    return 'Приветик'


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
    with open('To_Do_list.txt', 'a') as file:
        file.write(f'{phrase}\n')
    answer_function(f'Задача {phrase} записана в список дел')


def play_sound():
    files = os.listdir(r"C:\Users\Максим\Desktop\Music")
    if len(files) != 0:
        random_file = f'{choice(files)}'
        answer_function(f'Колбасимся под {random_file.split("/")[-1]}')
        os.startfile(fr"C:\Users\Максим\Desktop\Music\{random_file}")
        return f'Слушаем {random_file.split("/")[-1]}'
    else:
        answer_function('Музыки по адресу нет')
        return 'Музыки по адресу нет'


#######################

def internet_search():
    pass



def main():
    while True:
        phrase = listen_command()

        for key, value in list_commands['commands'].items():
            if phrase in value:
                print(globals()[key]())
            else:
                if type(list_commands['commands'][key]) is dict:
                    for key_c, value_c in list_commands['commands'][key].items():
                        if phrase in value_c:
                            print(globals()[key_c](phrase))
                        else:
                            print('Повтори фразу')

