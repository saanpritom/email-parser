"""Email parsers main functions.

Import these functions according to need and get parsed results.
"""
from enum import Enum
from email import policy as plc

# Local import
from parsers.parsers import Parser


class OutputType(Enum):
    """Results output type enum class.

    If new types of output cases are added then
    please add the new value here.
    """

    CONSOLE = 'console'
    TEXT = 'text'
    HTML = 'html'


default_output_type = OutputType.CONSOLE


def parse_email(email_file_path: str, encoding: str = "locale", policy: plc = plc.default,
                output_type: OutputType = default_output_type.value, output_file_path: str | None = None,
                fields: list | None = None):
    """Parse an email file and generate results."""
    if fields is None:
        fields = ['subject', 'from', 'to', 'date', 'body', 'attachment']
    if output_type == 'console':
        parser = Parser(file_path=email_file_path, encoding=encoding, policy=policy)
        return parser.get_results(fields)
