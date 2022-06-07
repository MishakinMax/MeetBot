from .libs.Classes import User as user
from .libs.Classes import Message
from .libs import HTTPMethods as http
from .libs import keyboard_presets
from .libs.Commands import *
from .libs.users_functions import *
from .libs.Classes import CallbackQuery



def state_to_login(users,message: Message, token):
    i = find_index_by_id(users, message.chat.id)
    users[i].state = "login_login"
    
    http.send_beautiful_message(token, message.chat.id, "Enter login", keyboard_presets.on_state_keyboard(),user = users, message =  message)
    return users


def state_to_link(users,message: Message, token):
    i = find_index_by_id(users, message.chat.id)
    users[i].state = "link"

    http.send_beautiful_message(token, message.chat.id, "Enter Link", keyboard_presets.on_state_keyboard(),user = users, message =  message)
    return users


def state_link(users,message: Message, token):
    if message.command == exit:
        users = disable_state(users, message, token)
        return users
    if message.command != None:
        http.send_beautiful_message(token, message.chat.id, "Enter link first or press exit", keyboard_presets.on_state_keyboard(),user = users, message =  message)
        return users

    i = find_index_by_id(users, message.chat.id)
    users[i].state = "start_checking"
    users[i].url = message.text

    http.send_beautiful_message(token, message.chat.id, "Starting browser",user = users, message =  message)
    return users

def none_exits(users,message: Message, token):
    users.append(user(message.chat.id))
    http.send_beautiful_message(token, message.chat.id, "Welcome", keyboard_presets.start_keyboard(),user = users, message =  message)
    return users


def state_login_login(users, message: Message, token):
    if message.command == exit:
        users = disable_state(users,message, token)
        return users

    if message.command != None:
        http.send_beautiful_message(token, message.chat.id, "Enter login first or press exit", keyboard_presets.on_state_keyboard(),user = users, message =  message)
        return users

    i = find_index_by_id(users, message.chat.id)
    users[i].state = "login_password"
    users[i].login = message.text

    http.send_beautiful_message(token, message.chat.id, "Enter Password", keyboard_presets.on_state_keyboard(),user = users, message =  message)
    return users


def state_login_password(users,message: Message, token):
    if message.command == exit:
        users = disable_state(users, message, token)
        return users

    if message.command != None:
        i = find_index_by_id(users, message.chat.id)
        http.send_beautiful_message(token, message.chat.id, "Enter password first or press exit", keyboard_presets.on_state_keyboard(),user = users, message =  message)
        return users

    i = find_index_by_id(users, message.chat.id)
    users[i].state = "none"
    users[i].password = message.text

    http.send_beautiful_message(token, message.chat.id, "login credentials saved", keyboard_presets.start_keyboard(),user = users, message =  message)
    return users


def disable_state(users, message: Message, token):
    i = find_index_by_id(users, message.chat.id)
    users[i].state = "none"

    http.send_beautiful_message(token, message.chat.id, "Menu!", keyboard_presets.menu_keyboard(),user = users, message =  message)
    return users

def state_start_checking(users, message: Message, token):
    http.send_beautiful_message(token, message.chat.id, "Wait until bot started",user = users, message =  message)
    return users

def state_on_checking(users, message: Message, token):
    if message.command != end:
        http.send_beautiful_message(token, message.chat.id, "You Can`t do anything while bot is running", keyboard_presets.on_check_keyboard(),user = users, message =  message)
        return users
    i = find_index_by_id(users, message.chat.id)
    users[i].state = "on_end"

    http.send_beautiful_message(token, message.chat.id, "Closing bot wait",user = users, message =  message)
    return users

def state_stop_checking(users, message: Message, token):
    http.send_beautiful_message(token, message.chat.id, "Wait until bot closed",user = users, message =  message)
    return users

def welcome_answer(users, message: Message, token):
    http.send_beautiful_message(token, message.chat.id, "Welcome!", keyboard_presets.menu_keyboard(),user = users, message =  message)
    return users

def wrong_command_answer(users, message: Message, token):
    http.send_beautiful_message(token, message.chat.id, "Wrong Command!", keyboard_presets.menu_keyboard(),user = users, message =  message)
    return users

state_command = {
    login: state_to_login,
    start: welcome_answer,
    menu: welcome_answer,
    look: state_to_link,
    exit: wrong_command_answer,
    end: wrong_command_answer
}

def state_none(users, message: Message, token):
    if message.command != None:
        return state_command[message.command](users, message, token)
    i = find_index_by_id(users, message.chat.id)

    http.send_beautiful_message(token, message.chat.id, "I can't speak without commands", keyboard_presets.menu_keyboard(),user = users, message =  message)


state_function = {
    "none" : state_none,
    "login_login": state_login_login,
    "login_password" : state_login_password,
    "link": state_link,
    "start_checking": state_start_checking,
    "on_check" : state_on_checking,
    "on_end" : state_stop_checking,
    "starting" : state_start_checking

}

def process_message(users,message: Message, token):
    i = find_index_by_id(users, message.chat.id)
    if i == -1:
        return none_exits(users, message, token)
    if type(message) is CallbackQuery:
        i = find_index_by_id(users, message.chat.id)

        http.answerCallbackQuery(token, message.id)
    return state_function[users[i].state](users, message, token)


