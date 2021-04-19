from selenium.webdriver.common.keys import Keys
import time


class RegistrationPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id = "reg_email"
        self.password_textbox_id = "reg_password"
        self.account_link_id = "//*[@id='menu-item-50']/a"
        self.register_name_btn = "register"
        self.login_error_show = "//*[@id='page-36']/div/div[1]/ul/li"

    def click_account(self):
        self.driver.find_element_by_xpath(self.account_link_id).click()

    def enter_mail(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_pass(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        time.sleep(3)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(Keys.TAB)

    def click_register(self):
        self.driver.find_element_by_name(self.register_name_btn).click()

    def invalid_register_msg(self):
        mes = self.driver.find_element_by_xpath(self.login_error_show).text
        return mes
