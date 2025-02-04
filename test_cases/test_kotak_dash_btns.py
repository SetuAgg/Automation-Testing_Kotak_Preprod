import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page
from base_pages.Kotak_Dashboard_tab import Kotak_Dashboard_Tab
from base_pages.Kotak_My_Learning_tab import Kotak_My_Learning_Tab




class Test_02_Kotak_Dash_Btns:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Testing button existence")
    def test_buttons(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        dash_tab = self.driver.find_element(By.XPATH,'//a[@class="nav-link"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",dash_tab)
        time.sleep(2)
        self.driver.click_dashboard_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_dashboard_btn.click_dashboard_tab()
        time.sleep(3)
        img = self.driver.find_element(By.XPATH,'//div[@class="card popup-home02 bannerCardDesktop"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", img)
        time.sleep(2)
        if img.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='dashboard_btn', attachment_type=AttachmentType.PNG)
            message_a = "Dashboard Button is working fine and test-case passed successfully.."
            allure.attach(message_a, name='dashboard_btn', attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='dashboard_btn', attachment_type=AttachmentType.PNG)
            message_b = "Dashboard Button is not working fine and test-case failed.."
            allure.attach(message_b, name='dashboard_btn', attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        my_learning_tab = self.driver.find_element(By.XPATH,"//a[text()='My Learning']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", my_learning_tab)
        time.sleep(2)
        club_privy = self.driver.find_element(By.XPATH,'//button[@class="btn btn-primary mt-2"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", club_privy)
        time.sleep(2)
        self.driver.click_club_privy_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_club_privy_btn.click_club_privy_btn()
        time.sleep(2)
        content = self.driver.find_element(By.XPATH,'//div[@class="innerPage"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", content)
        time.sleep(2)
        self.driver.click_bck_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_bck_btn.click_bck_btn()
        time.sleep(3)
        self.driver.click_feedback_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_feedback_btn.click_feedback_tab()
        time.sleep(2)
        box = self.driver.find_element(By.XPATH,'//div[@class="modal-content"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", box)
        time.sleep(3)
        if box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='feedback_btn', attachment_type=AttachmentType.PNG)
            message_e = "Feedback Button is working fine and test-case passed successfully.."
            allure.attach(message_e, name='feedback_btn', attachment_type=AttachmentType.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='feedback_btn', attachment_type=AttachmentType.PNG)
            message_f = "Feedback Button is not working fine and test-case failed.."
            allure.attach(message_f, name='feedback_btn', attachment_type=AttachmentType.TEXT)
            assert False
        time.sleep(2)
        skip_btn = self.driver.find_element(By.XPATH, '//button[@class="skipBtn btn btn-primary"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", skip_btn)
        self.driver.click_skip_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_skip_btn.click_skip_btn()
        time.sleep(2)
        self.driver.click_take_a_tour_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_take_a_tour_btn.click_take_a_tour_btn()
        time.sleep(3)
        dia_box = self.driver.find_element(By.XPATH,'//div[@class="__floater__body"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", dia_box)
        time.sleep(3)
        if dia_box.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='take_a_tour_btn', attachment_type=AttachmentType.PNG)
            message_g = "Take a Tour Button is working fine and test-case passed successfully.."
            allure.attach(message_g, name='take_a_tour_btn', attachment_type=AttachmentType.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='take_a_tour_btn', attachment_type=AttachmentType.PNG)
            message_h = "Take a Tour Button is not working fine and test-case failed.."
            allure.attach(message_h, name='take_a_tour_btn', attachment_type=AttachmentType.TEXT)
            self.driver.close()
            assert False

































