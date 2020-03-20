# -*- coding: utf-8 -*-

"""Documentation file date.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import re
import dateutil.parser
from datetime import datetime
from typing import NoReturn, Text, List, Dict
from resources.exception import IsoDateException

# =============================================================================
# CLASS DATETIME
# =============================================================================

class DateTime():

    def __init__(self, iso_date: Text) -> NoReturn:
        self._iso_date = iso_date if self.validate_iso_date_8601(iso_date) else None

    @staticmethod
    def validate_iso_date_8601(iso_date: Text) -> bool:
        regex = r"^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$"
        match_iso8601 = re.compile(regex).match
        try:
            if match_iso8601(iso_date): return True
        except:
            pass
        return False

    def convert_iso_date(self) -> List:
        if self.iso_date:
            return dateutil.parser.parse(self.iso_date).strftime("%m/%d/%Y, %H:%M:%S").split(",")
        else:
            raise IsoDateException("We don't have a ISO date 8601. Probably your date isn't a ISO date 8601...")

    def serialize(self) -> Dict:
        return {
            "iso_date_8601_last_updated"  : self.iso_date,
            "date_information_iso_date_8601_last_updated"  : self.date_information
        }
        
    @property
    def iso_date(self) -> Text:
        return self._iso_date

    @property
    def date_information(self) -> List:
        return self.convert_iso_date()
