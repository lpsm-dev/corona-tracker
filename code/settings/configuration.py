# -*- coding: utf-8 -*-

"""Documentation file configuration.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import os
from os import environ
from typing import NoReturn, Text
from settings.exception import ExceptionDefault

# =============================================================================
# CLASS - CONFIGURATION
#
# THIS CLASS HAVE A INHERITANCE WITH EXCEPTION DEFAULT CLASS
# =============================================================================

class Configuration(ExceptionDefault):

    def __init__(self) -> NoReturn:
        self._envs = {
                        "LOG_PATH": self._get_env_value("LOG_PATH"),
                        "LOG_FILE": self._get_env_value("LOG_FILE"),
                        "LOG_LEVEL": self._get_env_value("LOG_LEVEL"),
                        "LOGGER": self._get_env_value("LOGGER"),
                        "ENDPOINT_BING": self._get_env_value("ENDPOINT_BING"),
                        "ENDPOINT_REST_COUNTRIES": self._get_env_value("ENDPOINT_REST_COUNTRIES"),
                        "ENDPOINT_THE_TRACKER_VIRUS": self._get_env_value("ENDPOINT_THE_TRACKER_VIRUS"),
                        "TELEGRAM_TOKEN": self._get_env_value("TELEGRAM_TOKEN")
                    }

    def _check_if_env_exist_in_dict_envs(self, env: Text) -> bool:
        return True if env in self._envs.keys() else False

    @staticmethod
    def _get_env_value(env: Text) -> Text:
        try:
            return environ.get(env)
        except KeyError as error:
            print(f"Error get the value of the environment variable {env} - {error}")

    def get_env(self, env: Text) -> Text:
        check = lambda env: self._envs[env] if self._check_if_env_exist_in_dict_envs(env) else self.raise_exception(ValueError(f"The env {env} not exist in the default dict."))
        return check(env)
        