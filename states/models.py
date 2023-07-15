from aiogram.dispatcher.filters.state import StatesGroup, State

class KnowledgeBase(StatesGroup):
    ENTRY_STATE = State()

class GiveAccessSheet(StatesGroup):
    ENTRY_STATE = State()