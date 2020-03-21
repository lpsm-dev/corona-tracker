# -*- coding: utf-8 -*-

"""Documentation file main.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from settings.log import Log
from settings.configuration import Configuration

from actions.bing import BingCorona

from resources.date import DateTime
from resources.coordenadas import Coordenadas

from bot.telegram import TelegramBot

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# =============================================================================
# GLOBAL DEFINITION
# =============================================================================

config = Configuration()

log_path = config.get_env("LOG_PATH") if config.get_env("LOG_PATH") else None
log_file = config.get_env("LOG_FILE") if config.get_env("LOG_FILE") else None

logger = Log(log_path, log_file, config.get_env("LOG_LEVEL"), config.get_env("LOGGER")).logger

bing = BingCorona(config.get_env("ENDPOINT_BING"), logger)

telegram = TelegramBot(config.get_env("TELEGRAM_TOKEN"))

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    cprint(figlet_format("Corona", font="starwars"), "red", "on_yellow", attrs=["dark"])

    logger.info("Hey! We are inside the Container.")

    bing_corona_information = bing.get_data()

    status = bing_corona_information["status"]

    logger.info(f"Bing Corona Get Information Status - {status}")

    data = bing_corona_information["data"]

    total_cases_confirmed = data["totalConfirmed"]
    total_cases_deaths = data["totalDeaths"]
    total_cases_recovered = data["totalRecovered"]
    last_update = data["lastUpdated"]

    print("Global information...")

    print(f"Total Cases Confirmed {total_cases_confirmed}...")

    print(f"Total Cases Deaths {total_cases_deaths}...")

    print(f"Total Cases Recovered {total_cases_recovered}...")

    date = DateTime(last_update).serialize()

    day = date["date_information_iso_date_8601_last_updated"][0]
    hour = date["date_information_iso_date_8601_last_updated"][1]

    print(f"Last Update - Day Information - {day}...")
    print(f"Last Update - Hour Information - {hour}...")


    areas = data["areas"]

    for key, value in enumerate(areas):
        print(f"{key} - {value}\n")

    print("\npress CTRL + C to cancel.")
    telegram.main()
