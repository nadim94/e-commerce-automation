from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
import unittest
import HtmlTestRunner
import time
# from Pages.Loginpage import LoginPage
from Pages.Registrationpage import RegistrationPage


class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Driver\chrome\chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.get("http://practice.automationtesting.in/")

    def test_valid_registration(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        register = RegistrationPage(driver)
        register.click_account()
        time.sleep(3)
        register.enter_mail("46asr@gmail.com")
        register.enter_pass("Asdf#..1234$na123")
        time.sleep(3)
        register.click_register()
        title_name = driver.title
        self.assertEqual("My Account – Automation Practice Site", title_name, "PASS")

    def test_blank_email(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        register = RegistrationPage(driver)
        register.click_account()
        time.sleep(3)
        register.enter_mail("")
        register.enter_pass("Asdf#..1234$na123")
        register.click_register()
        time.sleep(3)
        msg = register.invalid_register_msg()
        self.assertEqual("Error: Please provide a valid email address.", msg, "PASS")

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        print("Test is Complete")


if __name__ == "__main__":
    unittest.main()
