# -*- coding: utf-8 -*-

"""Documentation file argparser.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import argparse
from typing import NoReturn, Text
from settings.exception import CreateParserException

# =============================================================================
# CLASS - ARGUMENTS
# =============================================================================

class Arguments:

    def __init__(self, *args, **kwargs) -> NoReturn:
        self._parser = self._create_parser_object(*args, **kwargs)
        self._build()

    @staticmethod
    def _create_parser_object(*args, **kwargs) -> argparse.ArgumentParser:
        try:
            return argparse.ArgumentParser(*args, **kwargs)
        except argparse.ArgumentError as error:
            print(f"Error when we create a parser object - {error}")
        except CreateParserException as error:
            print(f"Error general exception in create a parser object - {error}")

    def _adding_arguments(self) -> NoReturn:
        self._parser.add_argument("-t", "--token",
                                type=str,
                                metavar="<token>",
                                default=None,
                                help="Telegram Token")
        self._parser.add_argument("-world", "--world",
                                action="store_true",
                                help="World Information about COVID-19")
        self._parser.add_argument("-bot", "--bot",
                                action="store_true",
                                help="Enable Bot Telegram")
        self._parser.add_argument("-v", "--version",
                                action="store_true",
                                help="COVID-19 CLI Version")

    def _parser_args(self) -> argparse.ArgumentParser.parse_args:
        return self._parser.parse_args()

    def _build(self) -> NoReturn:
        self._adding_arguments()
        self._args = vars(self._parser_args())

    @property
    def args(self) -> Text:
        return self._args
