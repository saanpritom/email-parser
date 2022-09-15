"""Email parsers main functions.

Import these functions according to need and get parsed results.
"""
from email import policy as plc

# Local import
from parsers.parsers import Parser


def parse_email(email_file_path: str, encoding: str = "locale", policy: plc = plc.default,
                output_type: str = 'console', output_file_path: str | None = None, *fields):
    """Parse an email file and generate results."""
    if output_type == 'console':
        parser = Parser(file_path=email_file_path, encoding=encoding, policy=policy)
        return parser.get_results('subject', 'from', 'to', 'body')
