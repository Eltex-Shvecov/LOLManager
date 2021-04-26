import tkinter as tk


class LOLGui:
    """Класс реализующий главное окно приложения"""

    def __init__(self, lol_manager):
        self.LOL_Manager = lol_manager
        self.data_gui = {'avatars': [], 'creeps': [], 'items': [[] for _ in range(10)]}
        self.main_window = tk.Tk()
        self.button_connect = tk.Button(self.main_window)
        self.log_indicate = tk.Label(self.main_window)
        self.log_text = tk.Label(self.main_window)

        for i in range(10):
            avatars = tk.Label(self.main_window)
            creeps = tk.Label(self.main_window)
            self.data_gui['avatars'].append(avatars)
            self.data_gui['creeps'].append(creeps)

            for r in range(7):
                item = tk.Label(self.main_window)
                self.data_gui['items'][i].append(item)

    def configuration(self):

        # основное окно
        self.main_window.geometry('650x450')
        self.main_window.title('LOL Manager')
        self.main_window.resizable(False, False)
        self.main_window.config(bg='#041320')

        # индикатор логирования
        self.log_indicate.config(bg='yellow')
        self.log_text.config(bg='#041320', text='', fg='white', font='Arial 8')
        self.log_indicate.place(anchor='sw', x=13, y=437, width=15, height=15)
        self.log_text.place(anchor='sw', x=33, y=437, height=15)

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
            self.data_gui['avatars'][i].place(anchor='center', x=295, y=coordinate, width=50, height=50)
            self.data_gui['avatars'][i + 5].place(anchor='center', x=355, y=coordinate, width=50, height=50)
            self.data_gui['creeps'][i].place(anchor='center', x=245, y=coordinate)
            self.data_gui['creeps'][i + 5].place(anchor='center', x=405, y=coordinate)
            coordinate += 60

        # предметы
        coordinate_y = 50
        for i in range(5):
            coordinate_x = 205
            x_right = 445
            for r in range(7):
                self.data_gui['items'][i][r].config(bg='#041320')
                self.data_gui['items'][i + 5][r].config(bg='#041320')
                self.data_gui['items'][i][r].place(anchor='center', x=coordinate_x, y=coordinate_y, width=25, height=25)
                self.data_gui['items'][i + 5][r].place(anchor='center', x=x_right, y=coordinate_y, width=25, height=25)
                coordinate_x -= 30
                x_right += 30
            coordinate_y += 60

    def show(self):
        self.configuration()
        self.main_window.mainloop()

    def click_connect(self):
        if self.LOL_Manager.check_start_api_server():
            self.set_text_to_log('Server start', 'green')
            self.LOL_Manager.start_application(self)
        else:
            self.set_text_to_log('Match not started', 'red')

    def set_avatars(self, idx, img):
        self.data_gui['avatars'][idx].config(image=img)

    def set_creep_score(self, idx, score):
        self.data_gui['creeps'][idx].config(text=score)

    def set_items(self, idx, items):
        for i, item in enumerate(items):
            self.data_gui['items'][idx][i].config(image=item)

    def set_text_to_log(self, text='', color=''):
        if color != '':
            self.log_indicate.config(bg=color)

        self.log_text.config(text=text)
        self.update_window()

    def update_window(self):
        self.main_window.update()
