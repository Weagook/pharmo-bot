import os

def create_message_presentation(path) -> str:
    message_presentation = 'Выберите номер файла\n'
    counter = 1
    for pres in path:
        pres = pres.replace('.pdf', '').replace('_', ' ')
        message_presentation += f'{counter}. {pres}\n'
        counter += 1
    return message_presentation

TOKEN = os.environ.get('TOKEN')
MANAGER_ID = os.environ.get('MANAGER_ID')

# Пути и файлы
MAIN_DIR = os.getcwd()
SOURCE_DIR = os.path.join(MAIN_DIR, 'sources')
LIST_FILES = {}
MESSAGE_SOURCE = {}
PRES_DIRS = {
    'materials': os.path.join(SOURCE_DIR, 'materials'),
    'pediatrics': os.path.join(SOURCE_DIR, 'pediatrics'),
    'therapy': os.path.join(SOURCE_DIR, 'therapy'),
    'lore': os.path.join(SOURCE_DIR, 'lore'),
    'instructions': os.path.join(SOURCE_DIR, 'instructions')
}

for directory, path in PRES_DIRS.items():
    pres_list = os.listdir(path)
    MESSAGE_SOURCE[directory] = create_message_presentation(pres_list)

for directory, path in PRES_DIRS.items():
    LIST_FILES[directory] = os.listdir(path)

# Для работы с Google Sheets
CREDENTIALS_FILE = 'credentials.json' 
SCOPES = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
SPREADSHEET_NAME = 'Вопросы и ответы'
SPREADSHEET_ID = '18Pps6sDbv4AqDyy2QyXLrW1Ext4Aun8G9eAN6roQf6M'


