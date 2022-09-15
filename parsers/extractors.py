"""Extract and process various data from Message object."""
from email.message import Message


class MessageExtractor:
    """Base message extractor class.

    The primary purpose of this class is to extract information and then
    process the information if needed."""

    def extract(self, fields: list) -> dict:
        """Extract selected fields information from the message object."""
        results = {}
        for field in fields:
            if field != 'body' and field != 'attachment':
                results[field] = self.get_header_info(field)
            elif field == 'body':
                self.extract_body_info()
                results[field] = self.get_html_body_info()
            elif field == 'attachment':
                self.extract_body_info()
                results[field] = self.get_attachment_info()
        return results

    def extract_body_info(self) -> None:
        """Extract body info from the message object.

        Extracting body info is different from the header info extraction.
        Because it may need to handle the multipart problem.
        """
        if self.message and not self.bodyData:
            for payload in self.message.get_payload():
                for part in payload.walk():
                    if part.is_multipart() is False:
                        key = part.get_content_type()
                        self.bodyData[key] = []
                        self.bodyData[key].append(part.get_payload())

    def get_header_info(self, key) -> str:
        """Extract key info from the message object."""
        if self.message:
            return self.message.get(name=key)
        return ''

    def get_html_body_info(self) -> list:
        """Return text/html body payload information."""
        for key, value in self.bodyData.items():
            if key == 'text/html':
                return value
        return []

    def get_attachment_info(self) -> list:
        """Return attachment data info.

        It considers attachment body payload data whose key name is not
        text/plain or text/html.
        """
        attach_list = []
        for key, value in self.bodyData.items():
            if key != 'text/plain' and key != 'text/html':
                attach_list.append({key: value})
        return attach_list

    def __init__(self, message: Message | None = None) -> None:
        """Default constructor method."""
        self.message = message
        self.bodyData = {}

