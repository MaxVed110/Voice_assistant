# import commander
#
# class Assistant:
#
#     def __int__(self, name):
#         self.name = name
#
#     def run_assistant(self):
#
#         while True:
#             phrase = commander.listen_command()
#
#             for key, value in commander.list_commands['commands'].items():
#                 if phrase in value:
#                     print(globals()[key]())
#                 else:
#                     if type(commander.list_commands['commands'][key]) is dict:
#                         for key_c, value_c in commander.list_commands['commands'][key].items():
#                             if phrase in value_c:
#                                 print(globals()[key_c](phrase))
#                             else:
#                                 print('Повтори фразу')
#
