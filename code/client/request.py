# -*- coding: utf-8 -*-

"""Documentation file request.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from client.url import URL
from typing import Text, NoReturn, Callable
from client.exception import URLException, InvalidURL, RequestGetException, RequestGetStatusException

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import json

# =============================================================================
# CLASS - REQUEST RESPONSE
# =============================================================================

class RequestResponse:

    def __init__(self, response: Text) -> NoReturn:
        self.status = response.status_code 
        self.reason = response.reason
        self.json = response.json()

    def get_json(self):
        return self.json

# =============================================================================
# CLASS - REQUEST
#
# THIS CLASS HAVE A INHERITANCE WITH URL CLASS
# =============================================================================

class Request(URL):

    def __init__(self, url: Text, logger: Callable, is_secure=True, retry=False) -> NoReturn:
        if self.url_validator(url):
            if url.startswith ("http://") or url.startswith ("https://"):
                self._url = url
                if not is_secure:
                    self._url = self._url.replace("https", "http")
            else:
                raise URLException("We need a endpoint with https:// or http://...")
        else:
            raise InvalidURL(f"This URL {url} is invalid...")
        self._logger = logger
        self.headers = self._headers
        if retry:
            self.session = self.requests_retry_session()
        else:
            self.session = requests.Session()

    @staticmethod
    def requests_retry_session(retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None) -> requests.Session():
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def get(self) -> Text:
        try:
            response = requests.get(self.url, headers=self.headers)
            response = RequestResponse(response)
            if response.status == requests.codes.ok:
                self.logger.info(f"Success request - Status {response.status}")
                try:
                    response = response.get_json()
                    self.logger.info(f"Success get json data")
                    return {
                        "status": True,
                        "data": response
                    }
                except json.JSONDecodeError:
                    response = response.reason
                    self.logger.error(f"Error get json data")
                    return {
                        "status": False,
                        "data": "response"
                    }
            else:
                raise RequestGetStatusException(f"Invalid request - Status {response.status}")
                return {
                        "status": False,
                        "data": ""
                }
        except RequestGetException:
            self.logger.error("Error Resquest Get")
            return {
                    "status": False,
                    "data": ""
                }

    @property
    def url(self):
        return self._url

    @property
    def logger(self):
        return self._logger

    @property
    def _headers(self):
        return {"Content-Type": "application/json"}

    def __str__(self) -> Text:
        return f"""
┌──────────────────┬─────────────────────────────────
│ Requests URL:    │ {self._url if self._url else None}
└──────────────────┴─────────────────────────────────"""
