import os

def create_message_presentation() -> str:
    message_presentation = ''
    counter = 1
    for pres in LIST_PRES:
        message_presentation += f'[{counter}] - {pres}\n'
        counter += 1
    return message_presentation

# TOKEN = os.environ.get('TOKEN_TELEGRAM')
TOKEN = '6145310970:AAFV4_w-r9jKO1pkf4EpXonGqABrfEUWgrM'
MAIN_DIR = os.getcwd()
SOURCE_DIR = os.path.join(MAIN_DIR, 'sources')
LIST_PRES = os.listdir(SOURCE_DIR)
message_pres = create_message_presentation()

CREDENTIALS_FILE = 'credentials.json' 
SCOPES = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
SPREADSHEET_NAME = 'Вопросы и ответы'
SPREADSHEET_ID = '18Pps6sDbv4AqDyy2QyXLrW1Ext4Aun8G9eAN6roQf6M'


