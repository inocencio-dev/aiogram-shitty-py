from aiogram.dispatcher.filters.state import StatesGroup, State


class MenuState(StatesGroup):
    klass = State()
    spec = State()
    current_menu = State()
    prev_menu = State()
    prev_menu_yvo = State()
    back = State()
