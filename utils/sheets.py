import asyncio
import gspread_asyncio
from google.oauth2.service_account import Credentials
from config import CREDENTIALS_FILE, SPREADSHEET_NAME, SCOPES, SPREADSHEET_ID

def get_creds():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE)
    scoped = creds.with_scopes(SCOPES)
    return scoped

agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)

async def read_google_sheet(checked_object: str, revise: bool = False) -> str or bool:
    agc = await agcm.authorize()
    current_sheet = await agc.open_by_key(SPREADSHEET_ID)
    current_tab = await current_sheet.get_worksheet(0)
    data = await current_tab.batch_get(['A2:B100'])
    if revise:
        checked_object = checked_object.lower().replace(',', '').replace('?', '').replace('!', '').replace(' ', '')
        for row in data[0]:
            if row[0].lower().replace(',', '').replace('?', '').replace('!', '').replace(' ', '') == checked_object:
                return row[1]
        return False
    return data

async def give_access_sheet(email: str) -> None:
    agc = await agcm.authorize()
    await agc.insert_permission(
        file_id = SPREADSHEET_ID,
        value = email,
        role = 'writer',
        perm_type = 'user',
        notify = True
    )
