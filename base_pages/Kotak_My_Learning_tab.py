from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Kotak_My_Learning_Tab:
    my_learning_tab_Xpath = '//a[@class="nav-link "]'


    def __init__(self, driver):
        self.driver = driver

    def click_my_learning_tab(self):
        self.driver.find_element(By.XPATH,self.my_learning_tab_Xpath).click()








