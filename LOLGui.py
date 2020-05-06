import tkinter as tk


class LOLGui:
    """Класс реализующий главное окно приложения"""

    def __init__(self, lol_manager):
        self.LOL_Manager = lol_manager
        self.data_gui = {'avatars': [], 'creeps': []}
        self.main_window = tk.Tk()
        self.button_connect = tk.Button(self.main_window)

        for i in range(10):
            avatars = tk.Label(self.main_window)
            creeps = tk.Label(self.main_window)
            self.data_gui['avatars'].append(avatars)
            self.data_gui['creeps'].append(creeps)

    def configuration(self):

        # основное окно
        self.main_window.geometry('540x400')
        self.main_window.title('LOL Tracking')
        self.main_window.resizable(False, False)
        self.main_window.config(bg='#041320')

        # кнопка connect
        self.button_connect.config(font='Arial', command=self.click_connect)
        self.button_connect.config(bd=0, bg='#C89B3C', activebackground='#C89B3C', text='Connect', fg='#F0E6D2')
        self.button_connect.place(anchor='center', relx=0.5, rely=0.9)

        # аватарки игроков и крипстаты
        coordinate = 50
        for i in range(5):
            self.data_gui['creeps'][i].config(bg='#041320', font='Arial 11 bold', fg='yellow', text='--')
            self.data_gui['creeps'][i + 5].config(bg='#041320', font='Arial 11 bold', fg='yellow', text='--')
            self.data_gui['avatars'][i].config(bg='white')
            self.data_gui['avatars'][i + 5].config(bg='white')
            self.data_gui['avatars'][i].place(anchor='center', x=240, y=coordinate, width=50, height=50)
            self.data_gui['avatars'][i + 5].place(anchor='center', x=300, y=coordinate, width=50, height=50)
            self.data_gui['creeps'][i].place(anchor='center', x=190, y=coordinate)
            self.data_gui['creeps'][i + 5].place(anchor='center', x=350, y=coordinate)
            coordinate += 60

    def show(self):
        self.configuration()
        self.main_window.mainloop()

    def click_connect(self):
        if self.LOL_Manager.check_start_api_server():
            print('Server start')
            self.LOL_Manager.start_application(self)
        else:
            print('Error')

    def set_avatars(self, idx, img):
        self.data_gui['avatars'][idx].config(image=img)

    def update_window(self):
        self.main_window.update()
