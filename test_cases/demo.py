import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page


class Test_02_Kotak_Dash_Btns:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"


    def test_dash_buttons(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.click_cross_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_cross_btn.click_cross_btn()
        assert True
        self.driver.save_screenshot(".\\screenshots\\test_cross_btn.png")
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        img = self.driver.find_element(By.XPATH,'//div[@class="box d-flex align-items-baseline justify-content-center oboardg_pop_icon"]')
        if img.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_dashboard_btn.png")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_dashboard_btn.png")
            assert False
        self.driver.click_my_learning_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_learning_btn.click_my_learning_tab()
        time.sleep(3)
        text = self.driver.find_element(By.XPATH,'//div[@class="d-flex justify-content-center"]').text
        if text == "My Learning Journey":
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_btn.png")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_btn.png")
            assert False



