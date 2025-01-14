from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Kotak_My_Schedule_Tab:
    my_schedule_tab_Xpath = '//a[@class="nav-link"]'

    def __init__(self, driver):
        self.driver = driver

    def click_my_schedule_btn(self):
        self.driver.find_element(By.XPATH, self.my_schedule_tab_Xpath).click()
