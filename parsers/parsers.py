"""Main parsing scripts."""
from email import policy
from email.message import Message
from email.parser import Parser


class EmailParser:
    """Base email file parser class.

    The primary responsibility of this class is to parse an email message
    and return output as a Message object."""

    def parse(self) -> Message:
        """Parse email contents and convert it into a message object."""
        pass

    def __init__(self, file_path: str, encoding: str = "locale") -> None:
        """Default constructor method."""
        self.file = open(file=file_path, mode='r', encoding=encoding)
        self.encoding = encoding
        self.parser = Parser(policy=policy.default)


class EmailFileParser(EmailParser):
    """File based email parser class."""

    def parse(self) -> Message:
        """Parse email contents from file object and convert it into a message object."""
        return self.parser.parse(self.file)

