# -*- coding: utf-8 -*-

"""Documentation file coordenadas.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from dataclasses import dataclass
from typing import NoReturn, Text, Dict

# =============================================================================
# CLASS COORDENADAS
# =============================================================================

@dataclass(init=True, repr=True)
class Coordenadas:
    _lat: float
    _long: float

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
