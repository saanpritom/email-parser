"""File writing formatter classes."""
import fileinput


class FileWriteFormatter:
    """File write formatter class.

    This class dictates the laws and format to write
    a file.
    """

    def write_in_text_format(self) -> None:
        """Write file in a text format."""
        for key, value in self.data.items():
            if key != 'attachment':
                if isinstance(value, str):
                    self.file_obj.write(key + ': ' + value + '\n')
                elif isinstance(value, list):
                    self.file_obj.write(key + ':\n------------\n')
                    for item in value:
                        self.file_obj.write(item)
                    self.file_obj.write('\n---------------\n')
        self.file_obj.write('\n------------\n')
        self.file_obj.write('attachments:')
        for item in self.data['attachment']:
            for key, value in item.items():
                self.file_obj.write(key + ':\n------------\n')
                for dt in value:
                    self.file_obj.write(dt)
                self.file_obj.write('\n---------------\n')
        self.file_obj.write('\n------------\n')

    def write_in_html_format(self) -> None:
        """Write file in a html format."""
        for key, value in self.data.items():
            self.file_obj.write('<html>')
            self.file_obj.write('<head>')
            if key != 'attachment' and key != 'body':
                self.file_obj.write('<p>')
                self.file_obj.write(key + ': ' + value)
                self.file_obj.write('</p><br/>')
            self.file_obj.write('</head>')
            self.file_obj.write('<body>')
            self.file_obj.write('<div class="body">')
            if key == 'body':
                if isinstance(value, str):
                    self.file_obj.write(key + ': ' + value)
                    self.file_obj.write('<br/>')
                elif isinstance(value, list):
                    self.file_obj.write(key + ':<br/>------------<br/>')
                    for item in value:
                        self.file_obj.write(item)
                    self.file_obj.write('<br/>---------------<br/>')
            self.file_obj.write('</div>')
            self.file_obj.write('<div class="attachment">')
            if key == 'attachment':
                self.file_obj.write('<br/>------------<br/>')
                self.file_obj.write('<strong>attachments:</strong>')
                for item in self.data['attachment']:
                    for attach_key, attach_value in item.items():
                        self.file_obj.write(attach_key + ':<br/>------------<br/>')
                        for dt in attach_value:
                            self.file_obj.write(dt)
                        self.file_obj.write('<br/>---------------<br/>')
            self.file_obj.write('<br/>------------<br/>')
            self.file_obj.write('</div>')
        self.file_obj.write('</body>')
        self.file_obj.write('</html>')

    def write(self) -> None:
        """Perform the write operation."""
        if self.format_type == 'txt':
            self.write_in_text_format()
        self.write_in_html_format()

    def __init__(self, file_obj: fileinput, data: dict, format_type: str | None = 'txt') -> None:
        """Default constructor class.

        This class need to initiate with a file object with 'w' right access,
        a data dict contains the data to write and a format type in which format the data
        will be formatted.
        The valid value of the format_type is either 'txt' which is default or 'html'.
        """
        self.file_obj = file_obj
        self.data = data
        self.format_type = format_type

