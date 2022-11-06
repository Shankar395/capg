import re
import time

from Library.excel_library import Readexcel
from Library.config import Configuration


class BmsPage:
    read_xl = Readexcel()
    event_locators = read_xl.read_locators(Configuration.event_locators_sheet)

    def __init__(self, driver):
        self.driver = driver

    # def bengaluru(self, bengaluru):
    #     locator = self.event_locators["enter_bengaluru"]
    #     self.driver.find_element(*locator).send_keys(bengaluru)
    #     time.sleep(4)
    #
    # def click_bengaluru(self):
    #     locator = self.event_locators["click_on_bengaluru"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(4)
    #
    def click_on_events(self):
        locator = self.event_locators["click_on_events"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def click_on_browse(self):
        locator = self.event_locators["click_on_browse"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_on_Art_Beat_Bengaluru(self):
        locator = self.event_locators["Art_Beat_Bengaluru"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def click_on_Texture_painting(self):
        locator = self.event_locators["Texture_painting"]
        self.driver.find_element(*locator).click()

    def click_Book(self):
        locator = self.event_locators["Book"]
        self.driver.find_element(*locator).click()

    def click_on_Add(self):
        locator = self.event_locators["Add"]
        self.driver.find_element(*locator).click()

    def click_on_proceed(self):
        locator = self.event_locators["proceed"]
        self.driver.find_element(*locator).click()

    def enter_Name(self, name):
        locator = self.event_locators["Name"]
        self.driver.find_element(*locator).send_keys(name)

    def enter_phone_no(self, phoneno):
        if isinstance(phoneno, float):
            phone = str(int(phoneno))
        assert len(phoneno) == 10
        locator = self.event_locators["phone_no"]
        self.driver.find_element(*locator).send_keys(phoneno)

    def enter_Email(self, Email):
        locator = self.event_locators["Email"]
        self.driver.find_element(*locator).send_keys(Email)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def click_on_checkbox(self):
        locator = self.event_locators["checkbox"]
        self.driver.find_element(*locator).click()

    def click_on_submit(self):
        locator = self.event_locators["submit"]
        self.driver.find_element(*locator).click()

    def click_on_login_to_proceed(self):
        locator = self.event_locators["login_to_proceed"]
        self.driver.find_element(*locator).click()










