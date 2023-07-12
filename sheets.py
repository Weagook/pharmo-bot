# Подключаем библиотеки
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

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


CREDENTIALS_FILE = 'credentials.json' 
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с таблицами и 4 версию API 
spreadsheetId = '18Pps6sDbv4AqDyy2QyXLrW1Ext4Aun8G9eAN6roQf6M'
sheetId = 0 

# Проверка, возвращает ли значение из таблицы
ans = database_search('и так далее??')     
print(ans)



# results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheetId, body = {
#   "requests": [

#     # Задать ширину столбца A: 150 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": sheetId,
#           "dimension": "COLUMNS",  # Задаем ширину колонки
#           "startIndex": 0, # Нумерация начинается с нуля
#           "endIndex": 1 # Со столбца номер startIndex по endIndex - 1 (endIndex не входит!)
#         },
#         "properties": {
#           "pixelSize": 150 # Ширина в пикселях
#         },
#         "fields": "pixelSize" # Указываем, что нужно использовать параметр pixelSize  
#       }
#     },

#     # Задать ширину столбцов B и C: 150 пикселей
#     {
#       "updateDimensionProperties": {
#         "range": {
#           "sheetId": sheetId,
#           "dimension": "COLUMNS",
#           "startIndex": 1,
#           "endIndex": 2
#         },
#         "properties": {
#           "pixelSize": 150
#         },
#         "fields": "pixelSize"
#       }
#     }
#   ]
# }).execute()

# # Заполнение
# results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
#     "valueInputOption": "USER_ENTERED", # Данные воспринимаются, как вводимые пользователем (считается значение формул)
#     "data": [
#         {"range": "Главный лист!A1:B1",
#          "majorDimension": "ROWS",     # Сначала заполнять строки, затем столбцы
#          "values": [
#                     ['Вопрос', 'Ответ'], # Заполняем первую строку
#                    ]}
#     ]
# }).execute()


# spreadsheet = service.spreadsheets().create(body = {
#     'properties': {'title': 'Вопросы и ответы', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Главный лист',
#                                'gridProperties': {'rowCount': 100, 'columnCount': 15}}}]
# }).execute()
# spreadsheetId = spreadsheet['spreadsheetId'] # сохраняем идентификатор файла
# print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)