"""Extract and process various data from Message object."""
from email.message import Message


class MessageExtractor:
    """Base message extractor class.

    The primary purpose of this class is to extract information and then
    process the information if needed."""

    def get_header_info(self, key) -> str:
        """Extract key info from the message object."""
        return self.message.get(name=key)

    def get_body_info(self) -> list:
        """Extract body info from the message object.

        Extracting body info is different from the header info extraction.
        Because it may need to handle the multipart problem.
        """
        results = []
        for payload in self.message.get_payload():
            # Sometimes the inner payload can be a list.
            # So, for list only the first element will be picked.
            if isinstance(payload, list):
                results.append(self.get_payload_in_string(payload[0]))
            else:
                results.append(self.get_payload_in_string(payload))
        return results

    def get_payload_in_string(self, payload: Message) -> str:
        """Search upto N terms to find string format of a payload."""
        if isinstance(payload, str):
            return payload
        elif isinstance(payload, list):
            return self.get_payload_in_string(payload[0].get_payload())
        else:
            return self.get_payload_in_string(payload.get_payload())

    def extract(self, *fields) -> dict:
        """Extract selected fields information from the message object."""
        results = {}
        for field in fields:
            if field != 'body':
                results[field] = self.get_header_info(field)
            else:
                results[field] = self.get_body_info()
        return results

    def __init__(self, message: Message) -> None:
        """Default constructor method."""
        self.message = message
