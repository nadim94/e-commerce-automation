from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner
import time
from Pages.Loginpage import LoginPage
from Pages.Registrationpage import RegistrationPage
from Pages.Myaccount import MyAccount


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Driver\chrome\chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.get("http://practice.automationtesting.in/")

    def test_get_dashboard(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        my_acc = MyAccount(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        time.sleep(2)
        data = my_acc.get_dashboard()
        print(data)
        self.assertEqual("Dashboard", data, "PASS")
        my_acc.get_logout()

    def test_order_view(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        my_acc = MyAccount(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        time.sleep(2)
        my_acc.order_click()
        time.sleep(2)
        view_data2 = my_acc.get_order_view()
        print(view_data2)
        self.assertEqual("VIEW", view_data2, "PASS")
        my_acc.get_logout()

    def test_view_check(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        login = LoginPage(driver)
        my_acc = MyAccount(driver)
        login.click_account()
        time.sleep(3)
        login.enter_username("nadim@gmail.com")
        login.enter_password("Asdf#..1234$")
        login.click_login()
        time.sleep(2)
        my_acc.order_click()
        time.sleep(2)
        my_acc.view_click()
        title = driver.title
        self.assertEqual("My Account – Automation Practice Site", title, "PASS")

    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.quit()
        print("Test is Complete")


if __name__ == "__main__":
    unittest.main()
