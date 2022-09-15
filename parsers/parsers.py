"""Email parsers main classes.

Import these classes according to need and get parsed results.
First initiate the appropriate class and then call the 'get_results' method
to get results.
"""
from email import policy as plc

# Local import
from parsers.readers import EmailParser
from parsers.extractors import MessageExtractor


class Parser:
    """Base parser class."""

    def parse_email(self, *fields) -> dict:
        """Parse email components."""
        self.messageExtractor.message = self.emailParser.parse()
        return self.messageExtractor.extract(*fields)

    def get_results(self, *fields) -> dict:
        """Return results.

        The base class return results for console output.
        """
        return self.parse_email(*fields)

    def __init__(self, file_path: str, encoding: str, policy: plc) -> None:
        """Default constructor class."""
        self.emailParser = EmailParser(file_path, encoding, policy)
        self.messageExtractor = MessageExtractor()
