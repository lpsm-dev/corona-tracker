# -*- coding: utf-8 -*-

"""Documentation file coordenadas.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import NoReturn, Text, Dict

# =============================================================================
# CLASS COORDENADAS
# =============================================================================

class Coordenadas():

    def __init__(self, lat: float, long: float) -> NoReturn:
        self._lat = lat 
        self._long = long

    def serialize(self) -> Dict:
        return {
            "lat": self.lat,
            "longitude": self.long
        }

    @property
    def lat(self) -> Text:
        return self._lat

    @property
    def long(self) -> Text:
        return self._long

    def __str__(self) -> Text:
        return f"lat: {self.lat} - long: {self.long}"
