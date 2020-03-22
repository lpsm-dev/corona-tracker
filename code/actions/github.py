# =============================================================================
# IMPORTS
# =============================================================================

import csv
import requests
from cachetools import cached, TTLCache

# =============================================================================
# GLOBAL
# =============================================================================

CASOS_POR_CIDADE = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
CASOS_POR_ESTADO = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
CASOS_TOTAIS = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv"
BASE_URL = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-%s.csv"

# =============================================================================
# FUNCTIONS
# =============================================================================

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def get_brazil_information(vision):
    if isinstance(vision, str):
        vision = vision.lower()
        try:
            request = requests.get(BASE_URL % vision)
            if request.status_code == 200:
                return request.text
            else:
                return False
        except Exception as error:
            return False
    else:
        raise Exception("We need a string.")

def parse_to_csv(information):
    try:
        return list(csv.DictReader(information.splitlines()))
    except Exception as error:
        return False

def find_estado(estado, information):
    return [elemento for elemento in parse_to_csv(information) if elemento["state"] == estado.upper()][0]
    