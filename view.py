# import tkinter as tk
# import commander
# import core
#
#
# class View:
#
#     def __init__(self, asistant: core.Assistant):
#         self.assistant = asistant
#         self.window_assist = tk.Tk(className='Максон')
#
#         self.window_assist.columnconfigure(0, weight=1, minsize=250)
#         self.window_assist.rowconfigure('all', weight=1, minsize=250)
#
#         self.lab = tk.Label(text='Что хотим?',
#                             background='red',
#                             justify='left', wraplength=150, width=20, height=10)
#         self.lab.grid(row=1, column=0, padx=5, pady=10)
#
#         self.lab_to = tk.Label(text='text', background='blue', width=20, height=10)
#         self.lab_to.grid(row=2, column=0, padx=5, pady=10)
#
#         self.lab_to['text'] = 'xxxxx'
#
#         self.window_assist.mainloop()
#
#         self.assistant.run_assistant()
#
#     def print_greeting(self, text):
#         self.lab['text'] = self.lab_to['text']
#         self.lab_to['text'] = text
#




#if __name__ == '__main__':
   # v = View()

    # window = tk.Tk()
#
# frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
# frame1.pack()
#
# frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
# frame2.pack()
#
# frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
# frame3.pack()
#
# window.mainloop()
