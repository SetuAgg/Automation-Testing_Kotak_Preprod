from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Kotak_Dashboard_Page:
    dashboard_tab_Xpath = '//a[@class="nav-link"]'
    my_learning_tab_Xpath = '//a[@class="nav-link "]'
    my_schedule_tab_Xpath = '//a[@class="nav-link"]'
    bell_Xpath = '//img[@id="niit_logo_mob"]'
    feedback_tab_Xpath = '//div[@class="feedback--button contentDesktopView"]'
    take_a_tour_Xpath = '//div[@class="take-tour-button"]'
    cross_btn = '//button[@class="btn-close"]'
    club_privy_btn = '//button[@class="btn btn-primary mt-2"]'
    bck_btn = '//button[@class="btn btn-primary bckbtn"]'
    skip_btn = '//button[@class="skipBtn btn btn-primary"]'


    def __init__(self,driver):
        self.driver = driver

    def click_cross_btn(self):
        self.driver.find_element(By.XPATH,self.cross_btn).click()

    def click_dashboard_tab(self):
        self.driver.find_element(By.XPATH,self.dashboard_tab_Xpath).click()

    def click_my_learning_tab(self):
        self.driver.find_element(By.XPATH,self.my_learning_tab_Xpath).click()

    def click_my_schedule_tab(self):
        self.driver.find_element(By.XPATH,self.my_schedule_tab_Xpath).click()

    def click_bell_btn(self):
        self.driver.find_element(By.XPATH,self.bell_Xpath).click()

    def click_feedback_tab(self):
        self.driver.find_element(By.XPATH,self.feedback_tab_Xpath).click()

    def click_take_a_tour_btn(self):
        self.driver.find_element(By.XPATH,self.take_a_tour_Xpath).click()

    def click_club_privy_btn(self):
        self.driver.find_element(By.XPATH,self.club_privy_btn).click()

    def click_bck_btn(self):
        self.driver.find_element(By.XPATH,self.bck_btn).click()

    def click_skip_btn(self):
        self.driver.find_element(By.XPATH,self.skip_btn).click()





