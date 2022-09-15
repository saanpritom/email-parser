"""Email parsers main classes.

Import these classes according to need and get parsed results.
First initiate the appropriate class and then call the 'get_results' method
to get results.
"""
from email import policy as plc

# Local import
from parsers.scripts import get_file_name, execute_writing_to_file
from parsers.readers import EmailParser
from parsers.extractors import MessageExtractor


class Parser:
    """Base parser class."""

    def parse_email(self, fields: list) -> dict:
        """Parse email components."""
        self.messageExtractor.message = self.emailParser.parse()
        return self.messageExtractor.extract(fields)

    def get_results(self, fields: list) -> dict:
        """Return results.

        The base class return results for console output.
        """
        return self.parse_email(fields)

    def __init__(self, file_path: str, encoding: str, policy: plc) -> None:
        """Default constructor class."""
        self.emailParser = EmailParser(file_path, encoding, policy)
        self.messageExtractor = MessageExtractor()


class FileParser(Parser):
    """File parser class.

    This parser class extends the base Parser class to generate the output
    in a file but by default in a .txt file.
    On its constructor it takes one more argument called 'output_file_dir'
    where it will generate its output.
    """

    def write_to_a_file(self, data) -> str:
        """Write data to a text file and returns the file's path."""
        file_name = self.output_file_dir + '/' + get_file_name(data) + self.file_extension
        fp = open(file_name, 'w')
        execute_writing_to_file(fp, data)
        fp.close()
        return file_name

    def get_results(self, fields: list) -> dict:
        """Return generated file path as result."""
        return {'path': self.write_to_a_file(super(self.__class__, self).get_results(fields))}

    def __init__(self, file_path: str, output_file_dir: str, output_file_extension: str,
                 encoding: str, policy: plc) -> None:
        """Default constructor class."""
        self.output_file_dir = output_file_dir
        self.file_extension = output_file_extension
        super(self.__class__, self).__init__(file_path, encoding, policy)
