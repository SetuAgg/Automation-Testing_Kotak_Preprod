import pytest
import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_Dashboard_tab import Kotak_Dashboard_Tab
from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page

class Test05_Kotak_Dashboard_Tab:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboard_tab(self,setup):
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
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        img = self.driver.find_element(By.XPATH,
                                       '//div[@class="box d-flex align-items-baseline justify-content-center oboardg_pop_icon"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", img)
        time.sleep(5)
        if img.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='dashboard_tab', attachment_type=AttachmentType.PNG)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='dashboard_tab', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
    @allure.severity(allure.severity_level.BLOCKER)
    def test_banner_box(self,setup):
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
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        banner_box = self.driver.find_element(By.XPATH,'//div[@class="nobannerimage loading-stop"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", banner_box)
        if banner_box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='banner_box', attachment_type=AttachmentType.PNG)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='banner_box', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
    @allure.severity(allure.severity_level.NORMAL)
    def test_learning_section(self,setup):
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
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        learning_sec = self.driver.find_element(By.XPATH,'//div[@class="dashboard-learning-section"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);",learning_sec)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", learning_sec)
        time.sleep(5)
        if learning_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='learning_section', attachment_type=AttachmentType.PNG)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='learning_section', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_leaderboard_section(self,setup):
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
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        leaderboard_sec = self.driver.find_element(By.XPATH,'//div[@class="leaderboard_section"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);",leaderboard_sec)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", leaderboard_sec)
        time.sleep(5)
        if leaderboard_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='leaderboard_section', attachment_type=AttachmentType.PNG)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='leaderboard_section', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calender_view(self,setup):
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
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(2)
        calender_sec = self.driver.find_element(By.XPATH,'//div[@class="col-md-7 calen-section my-calender-main"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);",calender_sec)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", calender_sec)
        time.sleep(5)
        if calender_sec.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='calender_view', attachment_type=AttachmentType.PNG)
            self.driver.close()

        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='calender_view', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False



















