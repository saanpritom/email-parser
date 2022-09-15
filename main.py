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

text_file_output_dir = 'media/parsed/text'
html_file_output_dir = 'media/parsed/html'


def print_on_console():
    """Print results directly on the console."""
    print(parse_email(email_file_one))
    print(parse_email(email_file_two))
    print(parse_email(email_file_three))


def generate_text_output_file():
    """Generate text output file."""
    print(parse_email(email_file_one, output_type='txt', output_file_dir=text_file_output_dir))
    print(parse_email(email_file_two, output_type='txt', output_file_dir=text_file_output_dir))
    print(parse_email(email_file_three, output_type='txt', output_file_dir=text_file_output_dir))


def generate_html_output_file():
    """Generate text output file."""
    print(parse_email(email_file_one, output_type='html', output_file_dir=html_file_output_dir))
    print(parse_email(email_file_two, output_type='html', output_file_dir=html_file_output_dir))
    print(parse_email(email_file_three, output_type='html', output_file_dir=html_file_output_dir))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_on_console()
    generate_text_output_file()
    generate_html_output_file()





