"""Extract and process various data from Message object."""
from email.message import Message


class MessageExtractor:
    """Base message extractor class.

    The primary purpose of this class is to extract information and then
    process the information if needed."""

    def get_header_info(self, key) -> str:
        """Extract key info from the message object."""
        if self.message:
            return self.message.get(name=key)
        return ''

    def get_body_info(self) -> dict:
        """Extract body info from the message object.

        Extracting body info is different from the header info extraction.
        Because it may need to handle the multipart problem.
        """
        data = {}
        if self.message:
            for payload in self.message.get_payload():
                for part in payload.walk():
                    if part.is_multipart() is False:
                        key = part.get_content_type()
                        data[key] = []
                        data[key].append(part.get_payload())
        return data

    def extract(self, fields: list) -> dict:
        """Extract selected fields information from the message object."""
        results = {}
        for field in fields:
            if field != 'body':
                results[field] = self.get_header_info(field)
            else:
                results[field] = self.get_body_info()
        return results

    def __init__(self, message: Message | None = None) -> None:
        """Default constructor method."""
        self.message = message
