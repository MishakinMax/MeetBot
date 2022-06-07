class User:
    def __init__(self,id,login = " ",password = " ",state = "none",url = None,session = None,last_message = None, last_bot_message = None):
        self.id = id
        self.state = state
        self.session = session
        self.login = login
        self.password = password
        self.last_user_message = last_message
        self.last_bot_message = last_bot_message
        self.url = url

class Message:
    def __init__(self,update_id,message_id,sender,chat,date,command,text):

        self.update_id = update_id
        self.message_id = message_id
        self.date = date
        self.command = command
        self.text = text
        self.sender = sender
        self.chat = chat

    def __str__(self):
        text = "\n Message:\n"
        text += str(vars(self)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        text += "\n Chat:\n"
        text += str(vars(self.chat)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        text += "\n Sender:\n"
        text += str(vars(self.sender)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        return text


class Sender:
    def __init__(self,id,is_bot,first_name,last_name,username,language_code):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code


class Chat:
    def __init__(self,id,first_name,last_name,username,type):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.type = type

class CallbackQuery:
    def __init__(self,update_id,id,Sender,message,chat_instance,command):
        self.update_id = update_id
        self.id = id
        self.Sender = Sender
        self.message = message
        self.message_id = message.message_id
        self.chat_instance = chat_instance
        self.command = command
        self.chat = message.chat

    def __str__(self):
        text = "\n Callback Query:\n"
        text += str(vars(self)).replace(",", "\n  ").replace("}{", "\n  ").replace("{", "   ")
        text += "\n Message:\n"
        text += str(vars(self.message)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        text += "\n Chat:\n"
        text += str(vars(self.message.chat)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        text += "\n Sender:\n"
        text += str(vars(self.message.sender)).replace(",","\n  ").replace("}{","\n  ").replace("{","   ")
        return text
