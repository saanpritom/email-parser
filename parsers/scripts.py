"""Generic scripting functions.

These functions are acting like a re-usable tools.
"""
import string
import random


def get_file_name(data: dict) -> str:
    """Return a file name.

    It first tries to return the data's subject value as the file name
    but if not possible then return a random name.
    """
    if 'subject' in data:
        return data['subject']
    return ''.join(random.choices(string.ascii_letters, k=7))

