from commander import *


# Основной класс
class Assistant:

    def __init__(self, name: str):
        self.name = name
        self.microphone = Microphone()

    # Рабочий цикл
    def run_assistant(self):
        answer_function(f'Привет, я {self.name} что хотели?')
        n = 0
        while True:
            n += 1
            print(f'цикл {n}')
            phrase = self.microphone.listen_command()
            for key in list_commands['commands'].keys():
                if phrase in key:
                    print(phrase)
                    print()
                    print(list_commands['commands'][key]())
                    continue
                else:
                    print('Повтори фразу')
                    continue
