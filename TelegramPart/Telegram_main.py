from . import Settings
from .libs import HTTPMethods as http
from . import Message_Proccesor as procces
users = []


def look_for_update(token=Settings.Token):
    global users
    Mes = http.get_updates(token)
    for message in Mes["Messages"]:
        procces.process_message(users,message,token)
    for message in Mes["Callback_Query"]:
        procces.process_message(users,message,token)


def send_message(text, chat_id,keyboard = None, token=Settings.Token):
    global users
    answer = http.send_beautiful_message(token, chat_id, text, keyboard,users)
    return answer

