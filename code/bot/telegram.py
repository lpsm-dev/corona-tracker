# -*- coding: utf-8 -*-

"""Documentation file telegram.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from dataclasses import dataclass
from typing import NoReturn, Text
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

# =============================================================================
# CLASS TELEGRAM BOT
# =============================================================================

@dataclass(init=True)
class TelegramBot:
    _token: str

    @staticmethod
    def start(bot, update) -> NoReturn:
        response_message = """
        Bem vindo ao CoronaBot
        Para receber atualizações de hora em hora, 
        registre-se com o comando abaixo:
        /register
        """
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

    @staticmethod
    def unknown(bot, update) -> NoReturn:
        response_message = "Comando desconhecido :("
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message
        )

    def main(self) -> NoReturn:
        updater = Updater(token=self.token)

        dispatcher = updater.dispatcher

        dispatcher.add_handler(
            CommandHandler("start", self.start)
        )

        dispatcher.add_handler(
            MessageHandler(Filters.command, self.unknown)
        )

        updater.start_polling()

        updater.idle()

    @property
    def token(self) -> Text:
        return self._token
