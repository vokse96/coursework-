import json

import telebot

with open('config.json') as file:
    data = json.load(file)
TOCKEN = data['TOCKEN']


papa_chat = 993531546


class TelegramPost:
    TOKEN = TOCKEN
    GROUP_ID = papa_chat
    bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

    def send_text(self, text):
        self.bot.send_message(self.GROUP_ID, text=text)


def send_info(text):
    bot = TelegramPost()
    bot.send_text(text=text)

