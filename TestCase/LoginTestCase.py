from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time
from Pages.Loginpage import LoginPage
from Pages.Registrationpage import RegistrationPage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Driver\chrome\chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.get("http://practice.automationtesting.in/")

    def test_login_valid(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        title_name = driver.title
        self.assertEqual("My Account – Automation Practice Site", title_name, "PASS")

    def test_login_invalid(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("Asdf#....1234$")
        login.click_login()
        mes_test = login.invalid_login_msg()
        print(mes_test)
        self.assertEqual(
            "ERROR: The password you entered for the username nadim@gmail.com is incorrect. Lost your password?",
            mes_test, "PASS")

    def test_Blank_username(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        mes = login.invalid_login_msg()
        self.assertEqual("Error: Username is required.", mes, "PASS")

    def test_Blank_password(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("")
        login.click_login()
        mess = login.invalid_login_msg()
        print(mess)
        self.assertEqual("Error: Password is required.", mess, "PASS")

    def test_all_blank(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("")
        login.enter_password("")
        login.click_login()
        mess_blank = login.invalid_login_msg()
        print(mess_blank)
        self.assertEqual("Error: Username is required.", mess_blank, "PASS")

    """def test(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim1@gmail.com")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        ss = login.test_msg()
        print(ss)"""

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        print("Test is Complete")


if __name__ == "__main__":
    unittest.main()
