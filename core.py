from commander import *


class Assistant:
    def __int__(self, name):
        self.name = name

    def run_assistant(self):
        answer_function(f'Привет, я {self.name} что хотели?')
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
                    print('Повтори фразу')
                    continue
