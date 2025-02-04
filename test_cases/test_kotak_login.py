import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Kotak_Login_Page import Kotak_Login_Page
from test_cases.conftest import setup
import time


class Test_01_Kotak_Login:
    page_url = "https://kotakacademy-preprod.niit.com/"
    username = "deepalik@mailinator.com"
    password = "Kotak@123"
    invalid_username = "deepalik123@mailinator.com"
    invalid_password = "Kotak@12345"
    success_login_box_xpath = '//div[@class="modal-content"]'
    logo_Xpath = '//img[@class="Kotak-RM-logo"]'
    image_Xpath = '//div[@class="login_slider_img"]'





    @allure.title("Testing Login Page")
    def test_login_page(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        act_title = self.driver.title
        exp_title = "Kotak RM Academy"
        if act_title == exp_title:
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_title', attachment_type=AttachmentType.PNG)
            message1 = "Main title is visible and test-case passed successfully.."
            allure.attach(message1, name="main_title", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)
        act_welcome_txt = self.driver.find_element(By.XPATH,'//p[@class="welcome_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_welcome_txt)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='test_welcome_text', attachment_type=AttachmentType.PNG)
        message3 = "Welcome Text of login page is visible and test-case passed successfully.."
        allure.attach(message3, name="main_title", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)
        act_login_text = self.driver.find_element(By.XPATH,'//div[@class="login_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_login_text)
        time.sleep(2)
        assert True
        if act_login_text.is_displayed():
            allure.attach(self.driver.get_screenshot_as_png(), name='login_text_visibility', attachment_type=AttachmentType.PNG)
            message4 = "Login Text of login page is visible and test-case passed successfully.."
            allure.attach(message4, name="login_text", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='login_text_visibility', attachment_type=AttachmentType.PNG)
            message4 = "Login Text of login page is not visible and test-case failed.."
            allure.attach(message4, name="login_text", attachment_type=allure.attachment_type.TEXT)
        time.sleep(2)
        email_label = self.driver.find_element(By.XPATH,"//label[text()='Email Address']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", email_label)
        time.sleep(2)
        if email_label.is_displayed():
            allure.attach(self.driver.get_screenshot_as_png(),name="Label_Email",attachment_type=AttachmentType.PNG)
            message5 = "Email Label is visible and highlighted successfully.."
            allure.attach(message5,name="Label_Login",attachment_type= allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Label_Email", attachment_type=AttachmentType.PNG)
            message10 = "Email Label is not visible and highlighted.."
            allure.attach(message10, name="Label_Login", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        pass_label = self.driver.find_element(By.XPATH,"//label[text()='Password']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", pass_label)
        time.sleep(2)
        if email_label.is_displayed():
            allure.attach(self.driver.get_screenshot_as_png(), name="Pass_Label", attachment_type=AttachmentType.PNG)
            message11 = "Password Label is visible and highlighted successfully.."
            allure.attach(message11, name="Pass_Login", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Pass_Label", attachment_type=AttachmentType.PNG)
            message12 = "Password Label is not visible and highlighted.."
            allure.attach(message12, name="Pass_Label", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        act_forgot_password_text = self.driver.find_element(By.XPATH,"//a[text()='Forgot Password?']")
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_forgot_password_text)
        time.sleep(2)
        if act_forgot_password_text.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_password_text', attachment_type=AttachmentType.PNG)
            message6 = "Forgot Password Text of login page is visible and test-case passed successfully.."
            allure.attach(message6, name="forgot_password_text", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_password_text', attachment_type=AttachmentType.PNG)
            message7 = "Forgot Password Text of login page is not visible and test-case failed.."
            allure.attach(message7, name="forgot_password_text", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        self.driver.click_forgot_password_btn = Kotak_Login_Page(self.driver)
        self.driver.click_forgot_password_btn.click_forgot_password_btn()
        time.sleep(3)
        act_success = self.driver.find_element(By.XPATH,'//div[@class="modal-content custom-modal"]')
        if act_success.is_displayed():
            time.sleep(2)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_btn_click', attachment_type=AttachmentType.PNG)
            message8 = "Forgot button click of login page is working and visible and test-case passed successfully.."
            allure.attach(message8, name="forgot_password_btn", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_btn_click', attachment_type=AttachmentType.PNG)
            message9 = "Forgot button click of login page is not working and visible and test-case failed.."
            allure.attach(message9, name="forgot_password_btn", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        element3 = self.driver.find_element(By.XPATH,'//button[@class="btn-close"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",element3)
        time.sleep(2)
        self.driver.click_close_btn = Kotak_Login_Page(self.driver)
        self.driver.click_close_btn.click_close_btn()
        time.sleep(3)
        logo = self.driver.find_element(By.XPATH,self.logo_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'",logo)
        time.sleep(2)
        if logo.is_displayed():
            time.sleep(2)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_logo', attachment_type=AttachmentType.PNG)
            message10 = "Logo of login page is visible and test-case passed successfully.."
            allure.attach(message10, name="Logo_test", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_logo', attachment_type=AttachmentType.PNG)
            message11 = "Logo of login page is not visible and test-case failed.."
            allure.attach(message11, name="Logo_test", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(2)
        image = self.driver.find_element(By.XPATH,self.image_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'",image)
        time.sleep(5)
        if image.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_image', attachment_type=AttachmentType.PNG)
            message12 = "Image of login page is visible and test-case passed successfully.."
            allure.attach(message12, name="Image_test", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_image', attachment_type=AttachmentType.PNG)
            message13 = "Image of login page is not visible and test-case failed.."
            allure.attach(message13, name="Image_test", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        self.driver.click_eye_btn = Kotak_Login_Page(self.driver)
        self.driver.click_eye_btn.click_eye_btn()
        time.sleep(3)
        eye_btn = self.driver.find_element(By.XPATH,'//div[@class="show-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",eye_btn)
        time.sleep(2)
        if eye_btn.is_displayed():
            time.sleep(2)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_btn', attachment_type=AttachmentType.PNG)
            message14 = "Eye button of login page is visible and test-case passed successfully.."
            allure.attach(message14, name="Eye_btn_test", attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_btn', attachment_type=AttachmentType.PNG)
            message15 = "Eye button of login page is not visible and test-case failed.."
            allure.attach(message15, name="Eye_btn_test", attachment_type=allure.attachment_type.TEXT)
            assert False
        time.sleep(3)
        footer = self.driver.find_element(By.XPATH,'//div[@class="desktop-footer"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",footer)
        time.sleep(3)
        if footer.is_displayed():
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_footer', attachment_type=AttachmentType.PNG)
            message16 = "Footer of login page is visible and test-case passed successfully.."
            allure.attach(message16, name="Footer_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_footer', attachment_type=AttachmentType.PNG)
            message17 = "Footer of login page is not visible and test-case failed.."
            allure.attach(message17, name="Footer_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Testing successful Login of Login Page")
    def test_kotak_valid_login(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.username)
        self.login_lp.enter_password(self.password)
        self.login_lp.click_login_btn()
        time.sleep(5)
        self.driver.maximize_window()
        time.sleep(3)
        act_successful_login = self.driver.find_element(By.XPATH,'//div[@class=" content-logo kotak-brand"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", act_successful_login)
        if act_successful_login.is_displayed():
            time.sleep(2)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_valid_login', attachment_type=AttachmentType.PNG)
            message18 = "Valid Login condition of login page is satisfying and test-case passed successfully.."
            allure.attach(message18, name="Login_page_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_valid_login', attachment_type=AttachmentType.PNG)
            message19 = "Valid Login condition of login page is not satisfying and test-case failed.."
            allure.attach(message19, name="Login_page_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    def test_kotak_invalid_login(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.enter_username(self.invalid_username)
        self.login_lp.enter_password(self.invalid_password)
        self.login_lp.click_login_btn()
        self.driver.maximize_window()
        time.sleep(3)
        error_message = self.driver.find_element(By.XPATH, '//div[@class="mb-2 login-msg"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'", error_message)
        if error_message.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_invalid_login', attachment_type=AttachmentType.PNG)
            message20 = "Invalid Login condition of login page is satisfying and test-case passed successfully.."
            allure.attach(message20, name="Login_page_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_invalid_login', attachment_type=AttachmentType.PNG)
            message21 = "Invalid Login condition of login page is not satisfying and test-case failed.."
            allure.attach(message21, name="Login_page_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False







