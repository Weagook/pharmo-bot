import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from config import CREDENTIALS_FILE, spreadsheetId, sheetId

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

def give_acces(email) -> None:
    '''Выдача доступа'''
    driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
    access = driveService.permissions().create(
        fileId = spreadsheetId,
        body = {'type': 'user', 'role': 'writer', 'emailAddress': email},  # Открываем доступ на редактирование
        fields = 'id'
    ).execute()

def get_data() -> list:
    result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheetId,
    range='Главный лист!A2:B100' 
    ).execute()
    return result

def database_search(request) -> str or bool:
    result = get_data()
    request = request.lower().replace(',', '').replace('?', '').replace('!', '').replace(' ', '')
    for row in result['values']:
        if row[0].lower().replace(',', '').replace('?', '').replace('!', '').replace(' ', '') == request:
            return row[1]
    return False
