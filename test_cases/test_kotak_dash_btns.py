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


    def test_cross_button(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_cross_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_cross_btn.click_cross_btn()
        time.sleep(3)
        assert True
        self.driver.save_screenshot(".\\screenshots\\test_cross_btn.png")
        self.driver.close()

    def test_dashboard_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        img = self.driver.find_element(By.XPATH,'//div[@class="box d-flex align-items-baseline justify-content-center oboardg_pop_icon"]')
        if img.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_dashboard_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_dashboard_btn.png")
            self.driver.close()
            assert False

    def test_my_learning_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_learning_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_learning_btn.click_my_learning_tab()
        text = self.driver.find_element(By.XPATH,'//div[@class="d-flex justify-content-center"]').text
        if text == "My Learning Journey":
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_btn.png")
            self.driver.close()
            assert False

    def test_feedback_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_cross_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_cross_btn.click_cross_btn()
        time.sleep(5)
        self.driver.click_feedback_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_feedback_btn.click_feedback_tab()
        box = self.driver.find_element(By.XPATH,'//div[@class="modal-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", box)
        time.sleep(5)
        if box.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_feedback_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_feedback_btn.png")
            self.driver.close()
            assert False

    def test_take_a_tour_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_cross_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_cross_btn.click_cross_btn()
        time.sleep(5)
        self.driver.click_take_a_tour_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_take_a_tour_btn.click_take_a_tour_btn()
        dia_box = self.driver.find_element(By.XPATH,'//div[@class="__floater__body"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", dia_box)
        time.sleep(5)
        if dia_box.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_take_a_tour_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_take_a_tour_btn.png")
            self.driver.close()
            assert False

































