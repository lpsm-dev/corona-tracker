from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

class TelegramBot:

    def __init__(self, token, data):
        self.token = token
        self.data = data

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
        bot.send_message(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

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
        bot.send_message(chat_id=chat_id, text=world_information, reply_to_message_id=msg_id)

    def unknown(self, bot, update):
        response_message = "Meow? Comando desconhecido! =^._.^="
        bot.send_message(
            chat_id=update.message.chat_id,
            text=response_message)

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
            MessageHandler(Filters.command, self.unknown)
        )

        updater.start_polling()

        updater.idle()
