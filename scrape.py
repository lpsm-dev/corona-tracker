# =============================================================================
# IMPORTS
# =============================================================================

import requests
import csv

# =============================================================================
# GLOBAL
# =============================================================================

CASOS_POR_CIDADE = ""
CASOS_POR_ESTADO = ""
CASOS_TOTAIS = ""

from dateutil.parser import parse

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    - https://stackoverflow.com/a/25341965/7120095
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """

    try: 
        parse(string, fuzzy=fuzzy)
        return True
    except ValueError:
        return False

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    import dateutil.parser
    yourdate = dateutil.parser.parse("2020-03-19T23:39:25.937Z")
    print(yourdate)