import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page
from base_pages.Kotak_My_Schedule_tab import Kotak_My_Schedule_Tab

class Test_04_Kotak_My_Schedule_Tab:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"

    def test_my_schedule_tab(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_schedule_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_schedule_btn.click_my_schedule_tab()
        time.sleep(2)
        head = self.driver.find_element(By.XPATH,'//p[@class="lable-heading_search"]')
        if head.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_tab.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_tab.png")
            self.driver.close()
            assert False

    def test_calender_view(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_schedule_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_schedule_btn.click_my_schedule_tab()
        time.sleep(2)
        calender_sec = self.driver.find_element(By.XPATH,'//div[@class="rbc-time-view"]')
        if calender_sec.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_calender_view.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_calender_view.png")
            self.driver.close()
            assert False

    def test_short_calender_view(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_schedule_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_schedule_btn.click_my_schedule_tab()
        time.sleep(2)
        calender_sec = self.driver.find_element(By.XPATH,'//div[@class="side-calender session-calendar"]')
        if calender_sec.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_short_calender_view.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_short_calender_view.png")
            self.driver.close()
            assert False

    def test_back_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_schedule_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_schedule_btn.click_my_schedule_tab()
        time.sleep(2)
        back_btn = self.driver.find_element(By.XPATH,'//div[@class="calendar-bckbtn ms-0"]')
        if back_btn.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_back_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_back_btn.png")
            self.driver.close()
            assert False

    def test_main_content(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.click_my_schedule_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_my_schedule_btn.click_my_schedule_tab()
        time.sleep(2)
        main_content = self.driver.find_element(By.XPATH,'//div[@class="container position-relative"]')
        if main_content.is_displayed():
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_main_content.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_main_content.png")
            self.driver.close()
            assert False






