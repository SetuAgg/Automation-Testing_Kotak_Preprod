import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_My_Learning_tab import Kotak_My_Learning_Tab




class Test_03_Kotak_My_Learning_Tab:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"
    footer_Xpath = '//footer[@style="margin-left: 0px;"]'


    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("Tesing my learning tab existence")
    def test_my_learning_tab(self,setup):
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
        element = self.driver.find_element(By.XPATH,'//div[@class="d-flex justify-content-center"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element)
        time.sleep(3)
        if element.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='my_learning_btn', attachment_type=AttachmentType.PNG)
            message1 = "My Learning Button is working fine and test-case passed successfully.."
            allure.attach(message1,name="my_learning_btn_success",attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='my_leaning_btn', attachment_type=AttachmentType.PNG)
            message2 = "My Learning Button is not working and test-case failed.."
            allure.attach(message2, name="my_learning_btn_success", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        section = self.driver.find_element(By.XPATH,'//div[@class="img-box_nw"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section)
        time.sleep(3)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", section)
        time.sleep(3)
        if section.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='self_learning_img', attachment_type=AttachmentType.PNG)
            message3 = "The image is visible successfully and test-case passed successfully.."
            allure.attach(message3, name="self_learning_img", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='self_learning_img', attachment_type=AttachmentType.PNG)
            message4 = "The image is not visible and test-case failed.."
            allure.attach(message4, name="self_learning_img", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        block = self.driver.find_element(By.XPATH,'//div[@class="main-learning-block"]')
        self.driver.execute_script("arguments[0].style.border='3px solid red'", block)
        time.sleep(3)
        if block.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='main_learning_block', attachment_type=AttachmentType.PNG)
            message5 = "Learning Block is visible and test-case passed successfully.."
            allure.attach(message5, name="learning_block", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='main_learning_block', attachment_type=AttachmentType.PNG)
            message6 = "Learning Block is not visible and test-case failed.."
            allure.attach(message6, name="learning_block", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        back_btn = self.driver.find_element(By.XPATH,'//div[@class="bckbtn-main kotak_bckbtn-main"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", back_btn)
        time.sleep(3)
        if back_btn.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='back_btn', attachment_type=AttachmentType.PNG)
            message7 = "Back Button is working fine and test-case passed successfully.."
            allure.attach(message7, name="back_btn", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='back_btn', attachment_type=AttachmentType.PNG)
            message8 = "Back Button is not working and test-case failed.."
            allure.attach(message8, name="back_btn", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False































