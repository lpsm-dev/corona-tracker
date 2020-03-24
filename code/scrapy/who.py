# -*- coding: utf-8 -*-

"""Documentation file who.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from typing import List, Dict, Text
from dataclasses import dataclass, field

# =============================================================================
# CLASS - WORLD HEALTH ORGANIZATION
# =============================================================================

@dataclass(init=False, repr=True, eq=False, order=False, unsafe_hash=False, frozen=False)
class WorldHealthOrganization:
    url: str = field(repr=True, default="https://www.who.int/news-room/q-a-detail/q-a-coronaviruses")

    def get(self) -> Dict:
        try:
            response = requests.get(self.url)
            information = response.text
            if information:
                return {
                    "status": True,
                    "data": information
                }
            else:
                return {
                    "status": False,
                    "data": ""
                }
        except Exception:
            return {
                    "status": False,
                    "data": ""
                }

    def make_soup(self) -> Text:
        return BeautifulSoup(self.get()["data"], "html.parser") 

    def soup_list_information(self) -> List:
        return self.make_soup().find(class_="sf-accordion")

    def soup_list_questions(self, translate=False) -> List:
        information = self.soup_list_information()
        if translate:
            return [Translator().translate(question.contents[0].strip().encode("ascii", errors="ignore").decode("utf-8") , src="en", dest="pt").text
                        for question in information.find_all("a", class_="sf-accordion__link")]
        else:
            return [question.contents[0].strip().encode("ascii", errors="ignore").decode("utf-8")
                        for question in information.find_all("a", class_="sf-accordion__link")]

    def soup_list_answers(self, translate=False) -> List:
        information = self.soup_list_information()
        if translate:
            return [Translator().translate(answer.getText() .encode("ascii", errors="ignore").decode("utf-8") , src="en", dest="pt").text
                        for answer in information.find_all("p", class_="sf-accordion__summary")]
        else:
            return [answer.getText() .encode("ascii", errors="ignore").decode("utf-8")
                        for answer in information.find_all("p", class_="sf-accordion__summary")]
