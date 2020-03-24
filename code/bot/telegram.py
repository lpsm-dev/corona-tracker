# -*- coding: utf-8 -*-

"""Documentation file telegram.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
from utils.os import OSystem
import matplotlib.pyplot as plt
from telegram.ext.dispatcher import run_async
from scrapy.who import WorldHealthOrganization
from typing import NoReturn, Text, Dict, Callable
from actions.github import get_brazil_information, parse_to_csv
from telegram import (ReplyKeyboardMarkup, InlineKeyboardButton, 
                                InlineKeyboardMarkup)
from telegram.ext import (Updater, CommandHandler, Filters, 
                                MessageHandler, CallbackQueryHandler)
from constants.conversations import (START, REGISTER, HELP, INFO, ABOUT, 
                                        TRANSMISSION, SINTOMAS, PREVENTION, 
                                            TRATAMENTO, FAQ, DEV, UNKNOWN)

from database.database import RedisController

# =============================================================================
# GLOBAL
# =============================================================================

information = get_brazil_information("total")

CASOS_TOTAIS_BRASIL = parse_to_csv(information)
        
# =============================================================================
# CLASS TELEGRAM BOT
# =============================================================================

class TelegramBot:

    def __init__(self, token: Text, data: Dict, logger: Callable) -> NoReturn:
        self.token = token
        self.data = data
        self._logger = logger
        self.os = OSystem()
        self.redis = RedisController()

# =============================================================================

    def world(self, update, context):
        bot = context.bot
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

        if not self.os.check_if_is_dir("/usr/src/code/images"):
            self.os.create_directory("/usr/src/code/images")

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

    def image(self, update, context):
        bot = context.bot
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

    def brazil(self, update, context):
        bot = context.bot
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

    """def questions(self, bot, update):
        who = WorldHealthOrganization()
        questions = who.soup_list_questions()
        keyboard = [[KeyboardButton(question)] for index, question in enumerate(questions, start=1)]
        keyboard_markup = ReplyKeyboardMarkup(keyboard)
        bot.send_message(chat_id=update.message.chat_id,
                        text="COVID-19 Questions",
                        reply_markup=keyboard_markup)"""

# =============================================================================

    @run_async
    def start(self, update, context):
        bot = context.bot
        bot.send_message(chat_id=update.message.chat.id, text=START)

# =============================================================================

    @run_async
    def register(self, update, context):
        chat_id = update.message.chat.id
        bot = context.bot
        name = update.message.from_user.first_name
        try:
            self.redis.set(chat_id, name)
            self.logger.info(self.redis.all_keys())
        except Exception as error:
            print(error)
        bot.send_message(chat_id=chat_id, text=REGISTER)

# =============================================================================

    @run_async
    def help(self, update, context):
        bot = context.bot
        bot.send_message(chat_id=update.message.chat.id, text=HELP)

# =============================================================================

    @run_async
    def users(self, update, context):
        bot = context.bot
        try:
            quantidade = len(self.redis.all_keys())
        except Exception as error:
            print(error)
        message = f"""
✅ Atualmente temos {quantidade} usuários cadastrados!
        """
        bot.send_message(chat_id=update.message.chat.id, text=message)

# =============================================================================

    def info(self, update, context):
        user = update.message.from_user
        self.logger.info("User %s started the conversation to get Infortions About COVID-19.", user.first_name)
        keyboard = [[InlineKeyboardButton("💻 Dev", callback_data="0"),
                    InlineKeyboardButton("🧪 Tratamento", callback_data="1")],
                    [InlineKeyboardButton("📈 Prevenção", callback_data="2"),
                    InlineKeyboardButton("📋 Sintomas", callback_data="3")],
                    [InlineKeyboardButton("📻 Transmissão", callback_data="4"),
                    InlineKeyboardButton("🌐 Sobre", callback_data="5")]]
        keyboard_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(text=INFO, reply_markup=keyboard_markup)

# =============================================================================
    
    def button_info(self, update, context):
        query, bot = update.callback_query, context.bot
        data, information = int(query.data), [DEV, TRATAMENTO, PREVENTION, SINTOMAS, TRANSMISSION, ABOUT]
        bot.send_message(chat_id=query.message.chat_id,
                    message_id=query.message.message_id, text=information[data])
        return CallbackQueryHandler.END

# =============================================================================

    def unknown(self, update, context):
        bot.send_message(chat_id=update.message.chat_id, text=UNKNOWN)

# =============================================================================

    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

# =============================================================================

    def main(self):

        updater = Updater(token=self.token, use_context=True)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.start))

        dispatcher.add_handler(CommandHandler("register", self.register))

        dispatcher.add_handler(CommandHandler("help", self.help))

        dispatcher.add_handler(CommandHandler("users", self.users))

        dispatcher.add_handler(CommandHandler("world", self.world))

        dispatcher.add_handler(CommandHandler("brazil", self.brazil))

        dispatcher.add_handler(CommandHandler("image", self.image))

        dispatcher.add_handler(CommandHandler("info", self.info))

        dispatcher.add_handler(CallbackQueryHandler(self.button_info))

        dispatcher.add_handler(CommandHandler("help", self.help))

        dispatcher.add_handler(MessageHandler(Filters.command, self.unknown))

        dispatcher.add_error_handler(self.error)

        updater.start_polling()

        updater.idle()

# =============================================================================

    @property
    def logger(self):
        return self._logger
