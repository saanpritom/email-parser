"""Generic scripting functions.

These functions are acting like a re-usable tools.
"""
import fileinput
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


def execute_writing_to_file(fp: fileinput, data: dict) -> None:
    """Execute write operation to any kind of file."""
    for key, value in data.items():
        if key != 'attachment':
            if isinstance(value, str):
                fp.write(key + ': ' + value + '\n')
            elif isinstance(value, list):
                fp.write(key + ':\n------------\n')
                for item in value:
                    fp.write(item)
                fp.write('\n---------------\n')
    fp.write('\n------------\n')
    fp.write('attachments:')
    for item in data['attachment']:
        for key, value in item.items():
            fp.write(key + ':\n------------\n')
            for dt in value:
                fp.write(dt)
            fp.write('\n---------------\n')
    fp.write('\n------------\n')

