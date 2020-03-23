# -*- coding: utf-8 -*-

"""Documentation file telegram.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import telegram
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async

import numpy as np
import matplotlib.pyplot as plt

import os

from actions.github import get_brazil_information, parse_to_csv

from constants.conversations import INFO, FAQ, ABOUT, DEV

from scrapy.who import WorldHealthOrganization

from typing import NoReturn

# =============================================================================
# GLOBAL
# =============================================================================

information = get_brazil_information("total")

CASOS_TOTAIS_BRASIL = parse_to_csv(information)
        
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

# =============================================================================

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

    def brasil(self, bot, update):

        data = self.data
        brasil = data["brasil"]
        total_cases_confirmed = brasil["totalConfirmed"]
        total_cases_deaths = brasil["totalDeaths"]
        total_cases_recovered = brasil["totalRecovered"]
        last_update = brasil["lastUpdated"]

        chat_id = update.message.chat.id

        total = CASOS_TOTAIS_BRASIL[0]
        casos_totais = total["totalCases"]
        casos_totais_ms = total["totalCasesMS"]
        casos_totais_nao_confirmados_ms = total["notConfirmedByMS"]
        mortes = total["deaths"]
        fonte = total["URL"]

        brasil_information = f"""
O status do COVID-19 no Brasil: 

Casos Confirmados: {total_cases_confirmed}
Casos Recuperados: {total_cases_recovered}
Casos Fatais: {total_cases_deaths}
Casos Ativos: {total_cases_confirmed - total_cases_deaths - total_cases_recovered}

Atualização: {last_update}

Fonte: https://www.bing.com/covid/data

=================

Número de casos confirmados de COVID-19 no Brasil segundo o Ministério de Saúde.

Inclui os dados confirmados pela plataforma oficial do Ministério da Saúde e demais noticiados pela secretarias de saúde de cada estado.

Casos Totais: {casos_totais}
Casos Totais Ministério de Saúde: {casos_totais_ms}
Casos não confirmados pelo Ministério de Saúde: {casos_totais_nao_confirmados_ms}
Casos Fatais: {mortes}

Fonte: {fonte}
"""
        bot.send_message(chat_id=chat_id, text=brasil_information)

# =============================================================================

    @run_async
    def info(self, bot, update):
        chat_id = update.message.chat.id
        info_message = INFO
        bot.send_message(chat_id=chat_id, text=info_message)

# =============================================================================

    @run_async
    def faq(self, bot, update):
        chat_id = update.message.chat.id
        info_message = FAQ
        bot.send_message(chat_id=chat_id, text=info_message)

# =============================================================================

    @run_async
    def about(self, bot, update):
        chat_id = update.message.chat.id
        info_message = ABOUT
        bot.send_message(chat_id=chat_id, text=info_message)

# =============================================================================

    @run_async
    def dev(self, bot, update):
        chat_id = update.message.chat.id
        info_message = DEV
        bot.send_message(chat_id=chat_id, text=info_message)

# =============================================================================

    def questions(self, bot, update):
        who = WorldHealthOrganization()
        questions = who.soup_list_questions()
        keyboard = [[telegram.KeyboardButton(question)] for index, question in enumerate(questions, start=1)]
        keyboard_markup = telegram.ReplyKeyboardMarkup(keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                        text="COVID-19 Questions",
                        reply_markup=keyboard_markup)

# =============================================================================

    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

# =============================================================================

    def unknown(self, bot, update):
        response_message = "🐒 Melhoras Babuzinho 🐒"
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message)

# =============================================================================

    def main(self):

        updater = Updater(token=self.token)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("info", self.info))

        dispatcher.add_handler(CommandHandler("faq", self.faq))

        dispatcher.add_handler(CommandHandler("about", self.about))

        dispatcher.add_handler(CommandHandler("dev", self.dev))
        
        dispatcher.add_handler(CommandHandler("start", self.start))

        dispatcher.add_handler(CommandHandler("world", self.world))

        dispatcher.add_handler(CommandHandler("brasil", self.brasil))

        dispatcher.add_handler(CommandHandler("image", self.image))

        dispatcher.add_handler(CommandHandler("questions", self.questions))

        dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))

        dispatcher.add_error_handler(self.error)

        updater.start_polling()

        updater.idle()

    @property
    def logger(self):
        return self._logger
