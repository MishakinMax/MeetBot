from .ReplyMarkup import GetInlineKeyboard,GetButton


def start_keyboard():
    return GetInlineKeyboard(GetButton("login", "/login"), GetButton("Enter meet", "/look"))


def menu_keyboard():
    return GetInlineKeyboard(GetButton("login", "/login"), GetButton("Enter meet", "/look"))


def on_check_keyboard():
    return GetInlineKeyboard(GetButton("Stop checking", "/end"))

def on_state_keyboard():
    return GetInlineKeyboard(GetButton("Exit", "/exit"))
