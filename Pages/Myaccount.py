from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
import unittest


class MyAccount():
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_item = "//*[@id='page-36']/div/div[1]/nav/ul/li[1]/a"
        self.sign_out_item = "//a[contains(text(),'Logout')]"
        self.order_item = "//a[contains(text(),'Orders')]"
        self.order_view = "//a[@class='button view']"

    def get_dashboard(self):
        dash_name = self.driver.find_element_by_xpath(self.dashboard_item)
        dash = dash_name.text
        return dash

    def get_logout(self):
        self.driver.find_element_by_xpath(self.sign_out_item).click()

    def order_click(self):
        self.driver.find_element_by_xpath(self.order_item).click()

    def get_order_view(self):
        view_text = self.driver.find_element_by_xpath(self.order_view)
        text_data = view_text.text
        return text_data

    def view_click(self):
        self.driver.find_element_by_xpath(self.order_view).click()

