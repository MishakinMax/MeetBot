from selenium.webdriver.common.keys import Keys

def enter_meet(session, url: str):
    session.page(url)

    f = session.get_element_by_class("VfPpkd-T0kwCb").find_elements_by_tag_name("button")[0]
    f.click()

    f = session.get_element_by_class("XCoPyb").find_elements_by_tag_name("div")[0]
    f.click()


def login_to_google(session, login: str, password: str):
    session.page("https://accounts.google.com/")
    elem = session.get_clickable_by_name("identifier")
    elem.send_keys(login)
    session.get_clickable_by_XPATH('//*[@id="identifierNext"]/div/button').click()

    element = session.get_clickable_by_name("password")
    element.send_keys(password)
    session.get_clickable_by_XPATH('//*[@id="passwordNext"]/div/button').click()

    session.get_element_by_class("x7WrMb")


def toggle_people_list(session):
    f = session.get_element_by_XPATH('//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/span/button')
    f.click()


def toggle_chat(session):
    f = session.get_clickable_by_XPATH('//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button')
    f.click()


def get_people_list(session):
    s = session.get_element_by_XPATH('//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[2]/span/button').get_attribute("aria-pressed")
    if s != 'true':
        toggle_people_list(session)
    f = session.get_elements_by_class("zWGUib")
    names = []
    try:
        for x in f:
            names.append(x.get_attribute("innerHTML"))
    except:
        pass
    return names

def print_to_chat(session,text):
    s = session.get_element_by_XPATH('//*[@id="ow3"]/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button').get_attribute("aria-pressed")
    if s != 'true':
        toggle_chat(session)
    el = session.get_clickable_by_XPATH('//*[@id="bfTqV"]')
    el.send_keys(text,Keys.ENTER)



