from typing import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
import unittest
import HtmlTestRunner
import time
from Pages.Shopepage import ShopPage


class ShopTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:\Driver\chrome\chromedriver.exe")
        cls.driver.maximize_window()
        # cls.driver.get("http://practice.automationtesting.in/")

    def test_valid_filter(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop= ShopPage(driver)
        shop.shop_enter()
        time.sleep(5)
        shop.fil_func()
        shop.enter_filter()

    def test_android_page(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(2)
        shop.click_android()
        page_title = driver.title
        self.assertEqual("Android – Automation Practice Site", page_title, "PASS")

    def test_selenium_page(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(2)
        shop.click_selenium()
        page_title2 = driver.title
        print(page_title2)
        self.assertEqual("selenium – Automation Practice Site", page_title2, "PASS")

    def test_price_low_to_high(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(3)
        shop.click_drop_down_low_to_high()
        time.sleep(3)
        data = shop.price_low_to_high()
        print(data)
        self.assertEqual(data, "Yes, List is sorted.", "PASS")

    def test_price_high_to_low(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(3)
        shop.click_drop_down_high_to_low()
        time.sleep(3)
        data_txt = shop.price_high_to_low()
        self.assertEqual(data_txt, "Yes, List is sorted De Order.", "PASS")

    def test_add_basket(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(3)
        shop.click_add_basket()
        time.sleep(2)
        num_item = shop.item_from_basket()
        print(num_item)
        self.assertEqual("1 Item", num_item, "PASS")

    def test_shop_add(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(3)
        shop.click_add_basket()
        time.sleep(2)
        num_item = shop.item_from_basket()
        print(num_item)
        self.assertEqual("1 Item", num_item, "PASS")
        shop.click_item_view()
        time.sleep(2)
        shop.remove_from_basket()

    def test_view_item_link(self):
        driver = self.driver
        driver.get("http://practice.automationtesting.in/")
        shop = ShopPage(driver)
        shop.shop_enter()
        time.sleep(3)
        shop.click_add_basket()
        time.sleep(2)
        num_item = shop.item_from_basket()
        print(num_item)
        self.assertEqual("1 Item", num_item, "PASS")
        shop.click_item_view()
        time.sleep(2)
        shop.remove_from_basket()






