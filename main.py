"""The example application where the parsers package will be run.

Here the following kinds of demonstrations are given:
 -> Console based output
 -> Plain text file output
 -> HTML file output.
"""

from parsers import parse_email

email_file_one = 'media/uploaded/Automatic reply_ 122_ 122.eml'
email_file_two = 'media/uploaded/test oindri 10.42 am.eml'
email_file_three = 'media/uploaded/Test 2.eml'


def print_on_console():
    """Print results directly on the console."""
    print(parse_email(email_file_one))
    print(parse_email(email_file_two))
    print(parse_email(email_file_three))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_on_console()





