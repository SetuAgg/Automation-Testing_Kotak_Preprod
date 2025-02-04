import allure
import pytest
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.Kotak_Dashboard_page import Kotak_Dashboard_Page
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from base_pages.Kotak_Dashboard_page_Detailed import Kotak_Dashboard_page_Detailed

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
        element1 = self.driver.find_element(By.XPATH,'//div[@class="batchinfo"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element1)
        if element1.is_displayed():
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
        element4 = self.driver.find_element(By.XPATH,"//h3[text()='Stage Wise LP']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element4)
        if element4.is_displayed():
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
        element5 = self.driver.find_element(By.XPATH,"//p[text()='First Stage']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element5)
        if element5.is_displayed():
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
        element6 = self.driver.find_element(By.XPATH,"//p[text()='Second Stage']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element6)
        if element6.is_displayed():
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
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element7)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element7)
        if element7.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_head', attachment_type=AttachmentType.PNG)
            message13 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message13, name="test_stage_block_head", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_head', attachment_type=AttachmentType.PNG)
            message14 = "Element is not visible correctly and test-case failed.."
            allure.attach(message14, name="test_stage_block_head", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element2 = self.driver.find_element(By.XPATH,'//div[@class="box learning_progress"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element2)
        time.sleep(2)
        if element2.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_graph', attachment_type=AttachmentType.PNG)
            message13 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message13, name="test_stage_block_graph", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_stage_block_graph', attachment_type=AttachmentType.PNG)
            message14 = "Element is not visible correctly and test-case failed.."
            allure.attach(message14, name="test_stage_block_graph", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element9 = self.driver.find_element(By.XPATH,'//div[@class="main_dashboard_leaderboard"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element9)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element9)
        time.sleep(2)
        if element9.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message13 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message13, name="test_stage_block_graph", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message14 = "Element is not visible correctly and test-case failed.."
            allure.attach(message14, name="test_leaderboard_bar", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element10 = self.driver.find_element(By.XPATH, '//div[@class="col-md-7 calen-section my-calender-main"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element10)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element10)
        time.sleep(2)
        if element9.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message15 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message15, name="test_stage_block_graph", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message16 = "Element is not visible correctly and test-case failed.."
            allure.attach(message16, name="test_leaderboard_bar", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element11 = self.driver.find_element(By.XPATH,'//div[@class="position-relative eureka_main_section"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element10)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element10)
        time.sleep(2)
        if element11.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message17 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message17, name="test_stage_block_graph", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leaderboard_bar', attachment_type=AttachmentType.PNG)
            message18 = "Element is not visible correctly and test-case failed.."
            allure.attach(message18, name="test_leaderboard_bar", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element12 = self.driver.find_element(By.XPATH,'//div[@class="learner_experience_block sec-m-t"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element12)
        self.driver.execute_script("arguments[0].style.border='5px solid red'", element12)
        time.sleep(2)
        if element12.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leader_experience', attachment_type=AttachmentType.PNG)
            message19 = "Element is visible correctly and test-case passed successfully.."
            allure.attach(message19, name="test_leader_experience", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_leader_experience', attachment_type=AttachmentType.PNG)
            message20 = "Element is not visible correctly and test-case failed.."
            allure.attach(message20, name="test_leader_experience", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False
























