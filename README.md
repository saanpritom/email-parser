# Email File Parser

### Parse simple email's contents from any file and can generate parsed output in terminal, text file or in a html file

## Requirements:
- Python >= 3.10

## How to run:
- First clone the repo to your machine. To clone use the following command

```shell
git clone git@github.com:saanpritom/email-parser.git
```

- Insert to the repo directory with this command.

```shell
cd email-parser/
```

- Here you will find a file called **main.py**. Open the file and change the following values according to your need.

```text
email_file_one = 'path/to/your/first/email/file'
email_file_two = 'path/to/your/second/email/file'
email_file_three = 'path/to/your/third/email/file'

text_file_output_dir = 'path/to/your/text/output/file/directory/'
html_file_output_dir = 'path/to/your/html/output/file/directory/'
```

- That's it now it is ready to run. To run just run this command

```shell
python main.py
```

> If you are not on a virtualenv then run with this command.

```shell
python3 main.py
```

- And now check the output directories. You will get the outputs and the console output is printed on the console.


## Technical Discussions:

The scripts in **main.py** is just for run the project quickly. It is not a dependent script. The main app resides inside the **parsers** directory.
The app is independent can be integrated with any framework like (Django, Flask or FastAPI) or with raw Python.