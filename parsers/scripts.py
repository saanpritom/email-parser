"""Generic scripting functions.

These functions are acting like a re-usable tools.
"""
import string
import random
import base64
import os


def get_file_name(data: dict | str) -> str:
    """Return a file name.

    It first tries to return the data's subject value as the file name
    but if not possible then return a random name.
    """
    if 'subject' in data:
        return data['subject']
    return ''.join(random.choices(string.ascii_letters, k=7))


def build_image_from_text(image_dir_path: str, extension: str, data: str) -> str:
    """Convert string into an image and return path."""
    extension = '.' + extension.split('/')[1]
    file_name = get_file_name(data)
    image_file_name = image_dir_path + '/' + file_name + extension
    with open(image_file_name, "wb") as fp:
        fp.write(base64.decodebytes(bytes(data, 'UTF-8')))
    return os.path.abspath(image_file_name)


