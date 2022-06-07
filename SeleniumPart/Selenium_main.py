from . import settings
import time
from .libs import meet_api
from .libs import selenium_session as selenium


class Checker:
    def __init__(self, page: str, login: str = settings.login , password: str = settings.password):
        self.page = page
        self.login = login
        self.password = password
        self.participants = []
        self.session = None

    def start(self):
        try:
            self.session = selenium.Session()
            meet_api.login_to_google(self.session, self.login, self.password)
            meet_api.enter_meet(self.session, self.page)
            time.sleep(5)
            return "connected"
        except:
            self.session.driver.quit()
            return "error on start"

    def check(self):
        try:
            now_participants = meet_api.get_people_list(self.session)
            for x in now_participants:
                if x not in self.participants:
                    self.participants.append(x)
            return self.participants
        except:
            self.session.driver.quit()
            return "error on check"
    def chat(self,text):
        meet_api.print_to_chat(self.session,text)

    def close(self):
        self.session.driver.quit()
        return "closed"
