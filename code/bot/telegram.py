# -*- coding: utf-8 -*-

"""Documentation file telegram.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

import numpy as np
import matplotlib.pyplot as plt

import os

# =============================================================================
# CLASS TELEGRAM BOT
# =============================================================================

class TelegramBot:

    def __init__(self, token, data, logger):
        self.token = token
        self.data = data
        self._logger = logger

# =============================================================================

    def start(self, bot, update):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        user = update.message.from_user.username
        bot_welcome = f"""
Opa {user}! Tudo tranquilo??
Bem vindo ao Bot COVID19-Tracker!

Tenho como objetivo a coleta e exibição de informações sobre o Covid-19 ao redor do mundo e no Brasil.

Nossa principal meta é atingir o maior número de pessoas com o status dos casos e alertar para que todos fiquem em casa e respeitem a quarentena.

Para contribuir acesse o repositório desse código - GitHub: https://github.com/lpmatos/corona-tracker
"""
        bot.send_message(chat_id=chat_id, text=bot_welcome)

# =============================================================================

    def world(self, bot, update):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        user = update.message.from_user.username
        data = self.data
        total_cases_confirmed = data["total_cases_confirmed"]
        total_cases_deaths = data["total_cases_deaths"]
        total_cases_recovered = data["total_cases_recovered"]
        day = data["day"]
        hour = data["hour"]
        world_information = f"""
O status do Coronga ao redor do mundo é: 

Casos Confirmados: {total_cases_confirmed}
Casos Recuperados: {total_cases_recovered}
Casos Fatais: {total_cases_deaths}
Casos Ativos: {total_cases_confirmed - total_cases_deaths - total_cases_recovered}

Data Atualização: {day}
Hora Atualização: {hour}

Fonte: https://www.bing.com/covid/data
"""
        bot.send_message(chat_id=chat_id, text=world_information)

# =============================================================================

    def create_image(self):

        if not os.path.exists("/usr/src/code/images"):
            os.mkdir("/usr/src/code/images")

        cases=[u"CONFIRMADOS", u"RECUPERADOS", u"MORTES", u"ATIVOS"]

        data = self.data

        total_cases_confirmed = data["total_cases_confirmed"]
        total_cases_deaths = data["total_cases_deaths"]
        total_cases_recovered = data["total_cases_recovered"]
        ativos = total_cases_confirmed - total_cases_deaths - total_cases_recovered

        info = [int(total_cases_confirmed), int(total_cases_deaths), int(total_cases_recovered), int(ativos)]

        fig, ax = plt.subplots()

        width = 0.75

        ind = np.arange(len(info))

        ax.barh(ind, info, width, color="blue")

        ax.set_yticks(ind + width / 2)

        for i, v in enumerate(info):
            ax.text(v, i, " " + str(v), color="blue", va="center", fontweight="bold")

        ax.set_yticklabels(cases, minor=False)

        plt.title("Casos Coronga Virus no mundo")

        plt.xlabel("Quantidade", fontsize=5)

        plt.ylabel("Casos", fontsize=5)  

        plt.savefig("/usr/src/code/images/image.png", dpi=300, format="png", bbox_inches="tight")

        plt.close() 

    def image(self, bot, update):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        message = f"""
Opa, infelizmente não conseguimos gerar sua imagem..."""
        self.create_image()
        photo = photo=open("/usr/src/code/images/image.png", "rb")
        if photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        else:
            bot.send_message(chat_id=chat_id, text=message)

# =============================================================================

    def unknown(self, bot, update):
        response_message = "VAI TOMAR NO CU BABU"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message)

# =============================================================================

    def main(self):

        updater = Updater(token=self.token)

        dispatcher = updater.dispatcher
        
        dispatcher.add_handler(
            CommandHandler('start', self.start)
        )

        dispatcher.add_handler(
            CommandHandler('world', self.world)
        )

        dispatcher.add_handler(
            CommandHandler('image', self.image)
        )

        dispatcher.add_handler(
            MessageHandler(Filters.command, self.unknown)
        )

        updater.start_polling()

        updater.idle()

    @property
    def logger(self):
        return self._logger
