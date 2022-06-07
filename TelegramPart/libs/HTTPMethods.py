import requests,json
from .users_functions import *
from . import Converter as convert
offset = 0


def get_updates(token):
    global offset
    data = {"offset": offset}
    HTTPHeaders = {"Content-Type": "application/json"}
    MesRequest = requests.get("https://api.telegram.org/bot" + token + "/getUpdates", data=json.dumps(data),headers=HTTPHeaders).json()
    Mes = convert.ToMessages(MesRequest)
    offset = MesRequest["result"][len(MesRequest["result"])-1]["update_id"]+1 if (len(MesRequest["result"]) > 0) else offset
    return {"Messages" : Mes,"Callback_Query" : convert.ToCallbackQuery(MesRequest)}


def send_beautiful_message(token,chat_id,text,keyboard = None,user = None,message = None):
    r = send_message(token, chat_id, text, keyboard)
    i = find_index_by_id(user, chat_id)
    if(user != None):
        delete_message(token,chat_id,user[i].last_bot_message)
        user[i].last_bot_message = r["result"]["message_id"]
    if(message != None):
        delete_message(token, message.chat.id, message.message_id)

    return r


def send_message(token,chat_id,text,keyboard = None):

    HTTPHeaders = {"Content-Type": "application/json"}
    data= {
        "chat_id": str(chat_id),
        "text": str(text),
    }
    if(keyboard != None):
        data["reply_markup"] = keyboard
    r = requests.post("https://api.telegram.org/bot"+token+"/sendMessage",data=json.dumps(data),headers=HTTPHeaders).json()
    return r


def delete_message(token,chat_id,message_id):
    HTTPHeaders = {"Content-Type": "application/json"}
    data = {
        "chat_id": str(chat_id),
        "message_id": str(message_id),
    }
    r = requests.post("https://api.telegram.org/bot" + token + "/deleteMessage", data=json.dumps(data),
                      headers=HTTPHeaders)
    return r


def answerCallbackQuery(token,callback_query_id):
    HTTPHeaders = {"Content-Type": "application/json"}
    data= {
        "callback_query_id": str(callback_query_id),
    }
    r = requests.post("https://api.telegram.org/bot"+token+"/answerCallbackQuery",data=json.dumps(data),headers=HTTPHeaders)
    return r
