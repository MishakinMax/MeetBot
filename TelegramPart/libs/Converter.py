from . import Classes as Class


def ToSender(JSON):

    senmes = JSON
    sender = Class.Sender(senmes["id"], senmes["is_bot"], senmes.get("first_name",""), senmes.get("last_name",""), senmes.get("username",""),senmes["language_code"])
    return sender
def ToMessage(JSON,update_id = 0):
    message = JSON
    chatmes = message["chat"]
    newChat = Class.Chat(chatmes["id"], chatmes.get("first_name",""), chatmes.get("last_name",""), chatmes.get("username",""),
                         chatmes["type"])
    senmes = message["from"]
    sender = Class.Sender(senmes["id"], senmes["is_bot"], senmes.get("first_name",""), senmes.get("last_name",""), senmes.get("username",""),
                          None)
    command = None
    text = str(message["text"])
    if ("/" == message["text"][0]):
        command = str(message["text"]).split()[0]
        text = text.replace(command, "")
    mes = Class.Message(update_id, message["message_id"], sender, newChat, message["date"], command, text)
    return mes

def ToMessages(JSON):
    Messages = JSON["result"]
    ret = []
    for Mes in Messages:
        try:message = Mes["message"];message["text"]
        except KeyError:
            continue

        chatmes = message["chat"]
        newChat = Class.Chat(chatmes["id"], chatmes.get("first_name", ""), chatmes.get("last_name", ""),
                             chatmes.get("username", ""),
                             chatmes["type"])
        senmes = message["from"]
        sender = Class.Sender(senmes["id"], senmes["is_bot"], senmes.get("first_name",""), senmes.get("last_name",""), senmes.get("username",""),
                          senmes["language_code"])
        command = None
        text = str(message["text"])
        if("/" == message["text"][0]):
            command = str(message["text"]).split()[0]
            text = text.replace(command,"")
        mes = Class.Message(Mes["update_id"],message["message_id"],sender,newChat,message["date"],command,text)
        ret.append(mes)
    return ret
def ToCallbackQuery(JSON):
    Messages = JSON["result"]
    ret = []
    for Mes in Messages:
        try:message = Mes["callback_query"]
        except KeyError:
            continue
        ret.append(Class.CallbackQuery(Mes["update_id"],message["id"],ToSender(message["from"]),ToMessage(message["message"]),message["chat_instance"],message["data"]))
    return ret
