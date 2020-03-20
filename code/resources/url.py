# -*- coding: utf-8 -*-

"""Documentation file url.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import Text
from client.exception import URLTypeException

try:
    # Python 3
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

# =============================================================================
# CLASS - URL
# =============================================================================

class URL:

    @staticmethod
    def url_validator(url: Text) -> bool:
        if isinstance(url, str):
            try:
                result = urlparse(url)
                return all([result.scheme, result.netloc, result.path])
            except:
                return False
        else:
            raise URLTypeException(f"We speec a {type(str)} not a {type(url)}")
            return False
        