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

        # получение корректных имен персонажей
        with open("champion.json", "r", encoding='utf-8') as read_file:
            json_file = js.loads(read_file.read())

        data = json_file['data']
        for names_heroes, data in data.items():
            self.revers_name[data['name']] = names_heroes

    def update_data_game(self):
        """Получение всех данных матча"""

        try:
            self.Data = req.get(self.url, verify='riotgames.pem')
            self.Data = self.Data.json()
            return True
        except req.exceptions.RequestException:
            return False

    def check_start_api_server(self):
        """Проверка запущен ли матч"""

        try:
            self.Data = req.get(self.url, verify='riotgames.pem')
            self.Data = self.Data.json()
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

        for i in range(10):
            Gui.set_creep_score(i, '0')

        while self.update_data_game():
            all_players = self.Data['allPlayers']
            for idx, champion in enumerate(all_players):
                scores = champion['scores']
                creep_score = scores['creepScore']
                Gui.set_creep_score(idx, creep_score)

            Gui.update_window()

        print('Match is over')
