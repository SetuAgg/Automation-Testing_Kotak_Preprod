import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page
from base_pages.Kotak_Login_Page import Kotak_Login_Page


class Test_Kotak_Dashboard_InDetail:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"


    def test_text_01(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(2)
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
        element1 = self.driver.find_element(By.XPATH,"//span[text()='Stage Wise Batch']").text
        if element1 == "Stage Wise Batch":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_01', attachment_type=AttachmentType.PNG)
            message1 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message1, name="test_text_01", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_01', attachment_type=AttachmentType.PNG)
            message2 = "Text is not visible correctly and test-case failed.."
            allure.attach(message2, name="test_text_01", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.driver.click_cross_btn = Kotak_Dashboard_Page(self.driver)
        self.driver.click_cross_btn.click_cross_btn()
        time.sleep(3)
        element2 = self.driver.find_element(By.XPATH,"//span[text()='Batch Start Date:']").text
        if element2 == "Batch Start Date:":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_02', attachment_type=AttachmentType.PNG)
            message3 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message3, name="test_text_02", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_02', attachment_type=AttachmentType.PNG)
            message4 = "Text is not visible correctly and test-case failed.."
            allure.attach(message4, name="test_text_02", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element3 = self.driver.find_element(By.XPATH,"//span[text()='16 Oct,2024']']").text
        if element3 == "16 Oct,2024":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_03', attachment_type=AttachmentType.PNG)
            message5 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message5, name="test_text_03", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_03', attachment_type=AttachmentType.PNG)
            message6 = "Text is not visible correctly and test-case failed.."
            allure.attach(message6, name="test_text_03", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element4 = self.driver.find_element(By.XPATH,"//h3[text()='Stage Wise LP']").text
        if element4 == "Stage Wise LP":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_04', attachment_type=AttachmentType.PNG)
            message7 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message7, name="test_text_04", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_04', attachment_type=AttachmentType.PNG)
            message8 = "Text is not visible correctly and test-case failed.."
            allure.attach(message8, name="test_text_04", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element5 = self.driver.find_element(By.XPATH,"//p[text()='First Stage']").text
        if element5 == "First Stage":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_05', attachment_type=AttachmentType.PNG)
            message9 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message9, name="test_text_05", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_05', attachment_type=AttachmentType.PNG)
            message10 = "Text is not visible correctly and test-case failed.."
            allure.attach(message10, name="test_text_05", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element6 = self.driver.find_element(By.XPATH,"//p[text()='Second Stage']").text
        if element6 == "Second Stage":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_06', attachment_type=AttachmentType.PNG)
            message11 = "Text is visible correctly and test-case passed successfully.."
            allure.attach(message11, name="test_text_06", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_text_06', attachment_type=AttachmentType.PNG)
            message12 = "Text is not visible correctly and test-case failed.."
            allure.attach(message12, name="test_text_06", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        element7 = self.driver.find_element(By.XPATH,'//div[@class="stage_duration_block"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element7)
        if element7.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_head', attachment_type=AttachmentType.PNG)
            message13 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message13, name="test_stage_block_head", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_head', attachment_type=AttachmentType.PNG)
            message14 = "Element is not visible correctly and test-case failed.."
            allure.attach(message14, name="test_stage_block_head", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False












