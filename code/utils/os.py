# -*- coding: utf-8 -*-

"""Documentation file os.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from os import path, makedirs
from typing import NoReturn, Text

# =============================================================================
# CLASS - OS
# =============================================================================

class OS:

    @classmethod
    def check_if_is_dir(cls, directory: Text) -> bool:
        return True if path.isdir(directory) else False

    @classmethod
    def check_if_is_file(cls, file: Text) -> bool:
        return True if path.isfile(file) else False

    @classmethod
    def join_directory_with_file(cls, directory: Text, file: Text) -> Text:
        return str(path.join(directory, file))

    @classmethod
    def create_directory(cls, directory: Text) -> NoReturn:
        try:
            print(f"Creating the directory {directory}")
            makedirs(directory)
        except OSError:
            print(f"OSError in create the directory {directory} - {error}")
        except Exception as error:
            print(f"Error general exception in create the directory {directory} - {error}")

    @classmethod
    def create_file(cls, file: Text) -> NoReturn:
        try:
            print(f"Creating the file {file}.")
            with open(file, mode="w"): pass
        except Exception as error:
            print(f"Error general exception create the file {file} - {error}")
