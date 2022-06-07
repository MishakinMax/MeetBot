def GetInlineKeyboard(*args):
    inline = []
    for button in args:
        inline.append( {
            "text": button["text"],
            "callback_data": button["callback_data"]
        })
    KeyBoard =[inline]
    Repl = {
        "inline_keyboard": KeyBoard
    }
    return Repl
def GetButton(text,data):
    return {"text": text, "callback_data": data}
