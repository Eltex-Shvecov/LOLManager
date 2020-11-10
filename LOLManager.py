import requests as req
import json as js
import tkinter as tk
import time as tm


class LOLManager:
    """Класс реализующий обработку запросов API"""

    def __init__(self):
        self.revers_name = {}
        self.avatars = []
        self.items = [[] for _ in range(10)]
        self.Data = None
        self.url = 'https://127.0.0.1:2999/liveclientdata/allgamedata'

        # получение корректных имен персонажей
        with open("resource/champion.json", "r", encoding='utf-8') as read_file:
            json_file = js.loads(read_file.read())

        data = json_file['data']
        for names_heroes, data in data.items():
            self.revers_name[data['name']] = names_heroes

    def update_data_game(self):
        """Получение всех данных матча"""

        try:
            tm.sleep(1)
            self.Data = req.get(self.url, verify='resource/riotgames.pem')
            self.Data = self.Data.json()
            return True
        except req.exceptions.RequestException:
            return False

    def check_start_api_server(self):
        """Проверка запущен ли матч"""

        try:
            self.Data = req.get(self.url, verify='resource/riotgames.pem')
            self.Data = self.Data.json()
            if self.Data.get('allPlayers') is None:
                return False
            else:
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
            for clear_idx in range(10):
                self.items[clear_idx].clear()
            for idx, champion in enumerate(all_players):
                scores = champion['scores']
                creep_score = scores['creepScore']
                Gui.set_creep_score(idx, creep_score)

                items = champion['items']
                for item in items:
                    path = 'resource/items/' + str(item['itemID']) + '.png'
                    img_item = tk.PhotoImage(file=path)
                    self.items[idx].append(img_item)
            # items
            for idx_item in range(10):
                Gui.set_items(idx_item, self.items[idx_item])

            Gui.update_window()

        Gui.set_text_to_log('Match is over', 'green')
