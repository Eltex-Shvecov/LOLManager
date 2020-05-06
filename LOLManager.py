import requests as req
import json as js
import tkinter as tk


class LOLManager:
    """Класс реализующий обработку запросов API"""

    def __init__(self):
        self.revers_name = {}
        self.avatars = []
        self.Data = None
        self.url = 'https://127.0.0.1:2999/liveclientdata/allgamedata'
        with open("champion.json", "r", encoding='utf-8') as read_file:
            json_file = js.loads(read_file.read())
        read_file.close()

        data = json_file['data']
        for names_heroes, data in data.items():
            self.revers_name[data['name']] = names_heroes

    def update_data_game(self):
        try:
            self.Data = req.get(self.url, verify='riotgames.pem')
            self.Data = self.Data.json()
            return True
        except req.exceptions.RequestException:
            return False

    def check_start_api_server(self):
        try:
            self.Data = req.get(self.url, verify='riotgames.pem')
            return True
        except req.exceptions.RequestException:
            return False

    def start_application(self, Gui):
        self.update_data_game()
        all_players = self.Data['allPlayers']

        for player in all_players:
            path = 'resource/heroes/' + self.revers_name[player['championName']] + '.png'
            img = tk.PhotoImage(file=path)
            self.avatars.append(img)

        for idx in range(10):
            Gui.set_avatars(idx, self.avatars[idx])

        Gui.update_window()

        #while self.update_data_game():
           # pass
