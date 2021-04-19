from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


class ShopPage():
    def __init__(self, driver):
        self.driver = driver
        self.link_by_name = "//*[@id='menu-item-40']/a"
        self.filter_buttion_by_path = "//*[@id='woocommerce_price_filter-2']/form/div/div[2]/button"
        self.android_link_text = "//a[contains(text(),'Android')]"
        self.selenium_link_text = "//a[contains(text(),'selenium')]"
        self.drop_down_link = "//*[@id='content']/form/select"
        self.select_price_low = "//*[@id='content']/form/select/option[5]"
        self.add_basket = "//*[@id='content']/ul/li[6]/a[2]"
        self.item_on_basket = "//*[@id='wpmenucartli']/a/span[1]"
        self.remove_item_from_basket = "//a[@class='remove']"
        self.view_cart = "//span[@class= 'cartcontents']"

    def fil_func(self):
        sliders = self.driver.find_elements_by_class_name("ui-slider-handle")
        left_slider = sliders[0]
        right_slider = sliders[1]
        move = ActionChains(self.driver)
        # Moving the left slider
        move.click_and_hold(left_slider).move_by_offset(20, 0).release().perform()
        # Moving the right slider
        move.click_and_hold(right_slider).move_by_offset(-60, 0).release().perform()

    def shop_enter(self):
        self.driver.find_element_by_xpath(self.link_by_name).click()

    def enter_filter(self):
        self.driver.find_element_by_xpath(self.filter_buttion_by_path).click()

    def click_android(self):
        self.driver.find_element_by_xpath(self.android_link_text).click()

    def click_selenium(self):
        self.driver.find_element_by_xpath(self.selenium_link_text).click()

    def click_add_basket(self):
        self.driver.find_element_by_xpath(self.add_basket).click()

    def click_drop_down_low_to_high(self):
        element = self.driver.find_element_by_xpath(self.drop_down_link)
        drp = Select(element)
        time.sleep(3)
        drp.select_by_visible_text('Sort by price: low to high')

    def price_low_to_high(self):
        test_data = self.driver.find_elements_by_xpath("//span/span[@class='woocommerce-Price-amount amount']")
        list_data = []
        flag = 0
        test_list = []
        for item in test_data:
            print(item.text)
            list_data.append(item.text)
        test_list1 = test_list[:]
        test_list1.sort()
        if test_list1 == test_list:
            flag = 1
        if flag:
            text = "Yes, List is sorted."
        else:
            text = "No, List is not sorted."
        return text

    def click_drop_down_high_to_low(self):
        element = self.driver.find_element_by_xpath(self.drop_down_link)
        drp = Select(element)
        time.sleep(3)
        drp.select_by_visible_text('Sort by price: high to low')

    def price_high_to_low(self):
        test_data = self.driver.find_elements_by_xpath("//span/span[@class='woocommerce-Price-amount amount']")
        list_data = []
        flag = 0
        test_list = []
        for item in test_data:
            print(item.text)
            list_data.append(item.text)
        test_list1 = test_list[:]
        test_list1.sort(reverse=True)
        if test_list1 == test_list:
            flag = 1
        if flag:
            text = "Yes, List is sorted De Order."
        else:
            text = "No, List is not sorted."
        return text

    def item_from_basket(self):
        number_of_item = self.driver.find_element_by_xpath(self.item_on_basket)
        num_data = number_of_item.text
        return num_data

    def remove_from_basket(self):
        self.driver.find_element_by_xpath(self.remove_item_from_basket).click()

    def click_item_view(self):
        self.driver.find_element_by_xpath(self.view_cart).click()
