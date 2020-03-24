# -*- coding: utf-8 -*-

"""Documentation file handlers.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import logging
from pythonjsonlogger import jsonlogger
from abc import ABCMeta, abstractmethod
from typing import NoReturn, Text, List

# =============================================================================
# CLASS STRATEGY HANDLER
# =============================================================================

class StrategyHandler(metaclass=ABCMeta):

    @abstractmethod
    def handler(self, log_file: Text, log_level: Text, formatter: Text) -> NoReturn:
        pass

# =============================================================================
# CLASS BASE FILE HANDLER - STRATEGY (DESIGNER PATTERN)
#
# THIS CLASS HAVE A INHERITANCE WITH STRATEGY HANDLER CLASS
# =============================================================================

class BaseFileHandler(StrategyHandler):

    @staticmethod
    def handler(log_file: Text, log_level: Text, formatter: Text) -> logging.FileHandler:
        file_handler = logging.FileHandler(filename=log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(jsonlogger.JsonFormatter(formatter))
        return file_handler

# =============================================================================
# CLASS BASE STREAM HANDLER - STRATEGY (DESIGNER PATTERN)
#
# THIS CLASS HAVE A INHERITANCE WITH STRATEGY HANDLER CLASS
# =============================================================================

class BaseStreamHandler(StrategyHandler):

    @staticmethod
    def handler(log_file: Text, log_level: Text, formatter: Text) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(jsonlogger.JsonFormatter(formatter))
        return stream_handler

# =============================================================================
# CLASS CONTEXT
# =============================================================================

class ContextHandler:

    def __init__(self, strategy: StrategyHandler) -> NoReturn:
        self._strategy = strategy

    @property
    def strategy(self) -> StrategyHandler:
        return self._strategy

    def get_handler(self, log_file: Text, log_level: Text, formatter: Text) -> NoReturn:
        return self._strategy.handler(log_file, log_level, formatter)
