# =============================================================================
# IMPORTS
# =============================================================================

import requests

# =============================================================================
# GLOBAL
# =============================================================================

CASOS_POR_CIDADE = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
CASOS_POR_ESTADO = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
CASOS_TOTAIS = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv"

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    req = requests.get(url=CASOS_TOTAIS)

    if req.status_code == 200:
        print(req.text)
        