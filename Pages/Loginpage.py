
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "username"
        self.password_textbox_id = "password"
        self.account_link_id = "//*[@id='menu-item-50']/a"
        self.login_button_name = "login"
        self.login_error_show = "//*[@id='page-36']/div/div[1]/ul/li"
        self.test_data = "//li[contains(text(),'Password is required.')]"

    def click_account(self):
        self.driver.find_element_by_xpath(self.account_link_id).click()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()

    def invalid_login_msg(self):
        mes = self.driver.find_element_by_xpath(self.login_error_show).text
        return mes

    def test_msg(self):
        mess = self.driver.find_element_by_xpath(self.login_error_show).text
        return mess

