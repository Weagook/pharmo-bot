from aiogram.dispatcher.filters.state import StatesGroup, State

class KnowledgeBase(StatesGroup):
    ENTRY_STATE = State()
    GET_RESPONSE = State()

class ConnectOperator(StatesGroup):
    WAITING = State()
    CONNECT = State()

class GiveAccessSheet(StatesGroup):
    ENTRY_STATE = State()