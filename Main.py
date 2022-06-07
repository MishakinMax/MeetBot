import threading

import SeleniumPart.Selenium_main as selenium
import TelegramPart.Telegram_main as telegram
import TelegramPart.libs.keyboard_presets as keyboard
import time

async def main():
    pass

def starting(users):
    start_users = list((user for user in users if user.state == "start_checking"))

    for x in start_users:
        x.state = "starting"

    for x in start_users:
        if (x.login == " " or x.password == " "):
            x.session = selenium.Checker(x.url)
        else:
            x.session = selenium.Checker(x.url, x.login, x.password)

        answer = x.session.start()
        if(answer == "error on start"):
            x.state = "none"
            telegram.send_message("Error take place on starting, maybe bad login credentials", x.id, keyboard.menu_keyboard())
            continue

        telegram.send_message("Bot started", x.id, keyboard.on_check_keyboard())
        x.state = "on_check"


def check(users):
    check_users = (user for user in users if user.state == "on_check")
    for x in check_users:
        answer = x.session.check()
        if (answer == "error on check"):
            x.state = "none"
            telegram.send_message("Error take place while checking, maybe meeting ended\nHowever, there last records\n" + '\n'.join(map(str, x.session.participants)),
                                  x.id,
                                  keyboard.menu_keyboard())
            continue


def close(users):
    check_users = (user for user in users if user.state == "on_end")
    for x in check_users:
        telegram.send_message("List of participants:\n" +'\n'.join(map(str, x.session.participants)) + "\nBot stopped", x.id, keyboard.menu_keyboard())
        x.session.close()
        x.state = "none"


if __name__ == '__main__':
    user = []
    print("Starting bot")
    while True:
        telegram.look_for_update()

        x = threading.Thread(target=starting, args=(telegram.users,))
        x.start()

        check(telegram.users)
        close(telegram.users)
        time.sleep(1)


