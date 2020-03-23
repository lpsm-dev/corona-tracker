# -*- coding: utf-8 -*-

"""Documentation file exception.py"""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import NoReturn, Text

# =============================================================================
# CLASS - EXCEPTION DEFAULT
# =============================================================================

class ExceptionDefault(object):

    @staticmethod
    def raise_exception(exception: Text) -> NoReturn:
        raise exception

# =============================================================================
# CLASS SETTINGS EXCEPTION
# =============================================================================

class SettingsException(Exception):
    pass

# =============================================================================
# CLASS CREATE PARSER EXCEPTION
# =============================================================================

class CreateParserException(SettingsException):
    pass
