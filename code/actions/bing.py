# -*- coding: utf-8 -*-

"""Documentation file request.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from client.request import Request
from typing import NoReturn, Text, Callable

# =============================================================================
# CLASS - BING CORONA
#
# THIS CLASS HAVE A INHERITANCE WITH REQUEST CLASS
# =============================================================================

class BingCorona(Request):

    def __init__(self, endpoint: Text, logger: Callable, is_secure=True, retry=False) -> NoReturn:
        super().__init__(endpoint, logger, is_secure=True, retry=False)
        self._logger = logger

    def get_data(self):
        self.logger.info("Getting Corona data...")
        return self.get()

    @property
    def endpoint(self):
        return self._endpoint

    @property
    def logger(self):
        return self._logger

    def __str__(self) -> Text:
        return f"""
┌──────────────────┬─────────────────────────────────
│ Endpoint:        │ {self._endpoint if self._endpoint else None}
└──────────────────┴─────────────────────────────────"""
