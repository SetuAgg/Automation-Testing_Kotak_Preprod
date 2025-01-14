import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_My_Learning_tab import Kotak_My_Learning_Tab




class Test_03_Kotak_My_Learning_Tab:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"
    footer_Xpath = '//footer[@style="margin-left: 0px;"]'



    def test_my_learning_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_my_learning_tab = Kotak_My_Learning_Tab(self.driver)
        self.driver.click_my_learning_tab.click_my_learning_tab()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH,'//div[@class="d-flex justify-content-center"]').text
        time.sleep(3)
        if element == "My Learning Journey":
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_tab.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_my_learning_tab.png")
            self.driver.close()
            assert False

    def test_self_learning_img(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_my_learning_tab = Kotak_My_Learning_Tab(self.driver)
        self.driver.click_my_learning_tab.click_my_learning_tab()
        time.sleep(3)
        section = self.driver.find_element(By.XPATH,'//div[@class="img-box_nw"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section)
        time.sleep(5)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", section)
        time.sleep(5)
        if section.is_displayed():
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_learning_section.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_learning_section.png")
            self.driver.close()
            assert False

    def test_main_learning_block(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_my_learning_tab = Kotak_My_Learning_Tab(self.driver)
        self.driver.click_my_learning_tab.click_my_learning_tab()
        time.sleep(2)
        block = self.driver.find_element(By.XPATH,'//div[@class="main-learning-block"]')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", block)
        time.sleep(5)
        if block.is_displayed():
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_main_learning_block.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_main_learning_block.png")
            self.driver.close()
            assert False

    def test_back_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.click_my_learning_tab = Kotak_My_Learning_Tab(self.driver)
        self.driver.click_my_learning_tab.click_my_learning_tab()
        time.sleep(2)
        back_btn = self.driver.find_element(By.XPATH,'//div[@class="bckbtn-main kotak_bckbtn-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", back_btn)
        time.sleep(5)
        if back_btn.is_displayed():
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_back_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_back_btn.png")
            self.driver.close()
            assert False






























