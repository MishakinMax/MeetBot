from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec




class Session:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument('--disable-blink-features=AutomationControlled')
        #options.add_argument("--headless")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_experimental_option("prefs",{
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.notifications": 2
        })
        self.driver = webdriver.Chrome(chrome_options=options)



    def page(self, url: str):
        self.driver.get(url)

    def get_element_by_class(self, class_name: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return element

    def get_element_by_name(self, name: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, name))
        )
        return element

    def get_element_by_XPATH(self, XPATH: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, XPATH))
        )
        return element

    def get_elements_by_class(self, class_name: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, class_name))
        )
        return element

    def get_elements_by_name(self, name: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.NAME, name))
        )
        return element

    def get_element_by_name(self, XPATH: str):
        element = Wait(self.driver, 10).until(
            ec.presence_of_all_element_located((By.XPATH, XPATH))
        )
        return element

    def get_clickable_by_name(self, name: str):
        element = Wait(self.driver, 10).until(
            ec.element_to_be_clickable((By.NAME, name))
        )
        return element
    def get_clickable_by_XPATH(self, XPATH: str):
        element = Wait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, XPATH))
        )
        return element
    def get_clickable_by_class(self, class_name: str):
        element = Wait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        return element
    def try_to_get_by_XPATH(self, XPATH: str):
        try:
            self.driver.find_element(By.XPATH,XPATH)
            return True
        except:
            return False
    def try_to_get_by_class(self, class_name: str):
        try:
            self.driver.find_element(By.CLASS_NAME,class_name)
            print("Yes")
            return True
        except:
            print("No")
            return False




