# -*- coding: utf-8 -*-

"""Documentation file handlers.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import logging
from pythonjsonlogger import jsonlogger
from __future__ import annotations
from abc import ABC, abstractmethod

# =============================================================================
# CLASS - HANDLER
# =============================================================================

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

# =============================================================================
# CLASS BASE FILE HANDLER - STRATEGY (DESIGNER PATTERN)
# =============================================================================

class BaseFileHandler:

    @staticmethod
    def _base_configuration_log_file_handler(log_file, log_level, formatter) -> logging.FileHandler:
        file_handler = logging.FileHandler(filename=log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(jsonlogger.JsonFormatter(formatter))
        return file_handler

# =============================================================================
# CLASS BASE STREAM HANDLER - STRATEGY (DESIGNER PATTERN)
# =============================================================================

class BaseStreamHandler:

    def _base_configuration_log_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(self.log_level)
        stream_handler.setFormatter(jsonlogger.JsonFormatter(self.formatter))
        return stream_handler
