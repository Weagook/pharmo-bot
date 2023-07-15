import os

def create_message_presentation(path) -> str:
    message_presentation = 'Выберите номер файла\n'
    counter = 1
    for pres in path:
        pres = pres.replace('.pdf', '').replace('_', ' ')
        message_presentation += f'{counter}. {pres}\n'
        counter += 1
    return message_presentation

# TOKEN = os.environ.get('TOKEN_TELEGRAM')
TOKEN = '6145310970:AAFV4_w-r9jKO1pkf4EpXonGqABrfEUWgrM'
MAIN_DIR = os.getcwd()
SOURCE_DIR = os.path.join(MAIN_DIR, 'sources')
LIST_PRES = os.listdir(os.path.join(SOURCE_DIR, 'materials'))
LIST_PRES_PEDIATRICS = os.listdir(os.path.join(SOURCE_DIR, 'pediatrics'))
LIST_PRES_LORE = os.listdir(os.path.join(SOURCE_DIR, 'lore'))
LIST_PRES_THERAPY = os.listdir(os.path.join(SOURCE_DIR, 'therapy'))
LIST_PRES_INSTRUCTION = os.listdir(os.path.join(SOURCE_DIR, 'instructions'))
message_source_pres = create_message_presentation(LIST_PRES)
message_pres_pediatrics = create_message_presentation(LIST_PRES_PEDIATRICS)
message_pres_therapy = create_message_presentation(LIST_PRES_THERAPY)
message_pres_lore = create_message_presentation(LIST_PRES_LORE)
message_pres_instr = create_message_presentation(LIST_PRES_INSTRUCTION)



CREDENTIALS_FILE = 'credentials.json' 
SCOPES = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
SPREADSHEET_NAME = 'Вопросы и ответы'
SPREADSHEET_ID = '18Pps6sDbv4AqDyy2QyXLrW1Ext4Aun8G9eAN6roQf6M'
MANAGER_ID = 1373643498
