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
    success_login_id = "example-custom-modal-styling-title"


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Testing Login Page Title")
    def test_title(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        act_title = self.driver.title
        exp_title = "Kotak RM Academy"
        if act_title == exp_title:
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_title', attachment_type=AttachmentType.PNG)
            message1 = "Main title is visible and test-case passed successfully.."
            allure.attach(message1, name="main_title", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_title', attachment_type=AttachmentType.PNG)
            message2 = "Main title is not visible and test-case failed.."
            allure.attach(message2, name="main_title", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Testing Welcome Text of Login Page")
    def test_welcome_text(self,setup):
        self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        act_welcome_txt = self.driver.find_element(By.XPATH,'//p[@class="welcome_text"]').text
        assert act_welcome_txt == "Kotak RM Academy",f"Expected welcome text to be 'Kotak RM Academy' but got {act_welcome_txt}"
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name='test_welcome_text', attachment_type=AttachmentType.PNG)
        message3 = "Welcome Text of login page is visible and test-case passed successfully.."
        allure.attach(message3, name="main_title", attachment_type=allure.attachment_type.TEXT)
        self.driver.close()


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Testing Login Text of Login Page")
    def test_login_text_visible(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        act_login_text = self.driver.find_element(By.XPATH,'//div[@class="login_text"]').text
        if act_login_text == "LOGIN":
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='login_text_visibility', attachment_type=AttachmentType.PNG)
            message4 = "Login Text of login page is visible and test-case passed successfully.."
            allure.attach(message4, name="login_text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='login_text_visibility', attachment_type=AttachmentType.PNG)
            message5 = "Login Text of login page is not visible and test-case failed.."
            allure.attach(message5, name="login_text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Testing Forgot Password Text of Login Page")
    def test_forgot_password_text(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        act_forgot_password_text = self.driver.find_element(By.XPATH,'//div[@class="forgot_password_text"]').text
        if act_forgot_password_text == "Forgot Password?":
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_password_text', attachment_type=AttachmentType.PNG)
            message6 = "Forgot Password Text of login page is visible and test-case passed successfully.."
            allure.attach(message6, name="forgot_password_text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_password_text', attachment_type=AttachmentType.PNG)
            message7 = "Forgot Password Text of login page is not visible and test-case failed.."
            allure.attach(message7, name="forgot_password_text", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False


    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Testing Forgot Password Button click of Login Page")
    def test_forgot_btn_click(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.click_forgot_password_btn()
        act_success_text = self.driver.find_element(By.XPATH,'//p[@class="reset_paswd_text"]').text
        if act_success_text == ("Lost your password? Please enter your Email Address, "
                                "a link will be sent to reset your password."):
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_btn_click', attachment_type=AttachmentType.PNG)
            message8 = "Forgot button click of login page is working and visible and test-case passed successfully.."
            allure.attach(message8, name="forgot_password_btn", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='forgot_btn_click', attachment_type=AttachmentType.PNG)
            message9 = "Forgot button click of login page is not working and visible and test-case failed.."
            allure.attach(message9, name="forgot_password_btn", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Testing Logo visibility of Login Page")
    def test_logo(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        logo = self.driver.find_element(By.XPATH,self.logo_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'",logo)
        time.sleep(5)
        if logo.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_logo', attachment_type=AttachmentType.PNG)
            message10 = "Logo of login page is visible and test-case passed successfully.."
            allure.attach(message10, name="Logo_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_logo', attachment_type=AttachmentType.PNG)
            message11 = "Logo of login page is not visible and test-case failed.."
            allure.attach(message11, name="Logo_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.title("Testing Image visibility of Login Page")
    def test_image_verification(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        image = self.driver.find_element(By.XPATH,self.image_Xpath)
        self.driver.execute_script("arguments[0].style.border='5px solid red'",image)
        time.sleep(5)
        if image.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_image', attachment_type=AttachmentType.PNG)
            message12 = "Image of login page is visible and test-case passed successfully.."
            allure.attach(message12, name="Image_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_image', attachment_type=AttachmentType.PNG)
            message13 = "Image of login page is not visible and test-case failed.."
            allure.attach(message13, name="Image_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Testing Eye button visibility of Login Page")
    def test_eye_btn(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.click_eye_btn()
        time.sleep(3)
        eye_btn = self.driver.find_element(By.XPATH,'//div[@class="show-password"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",eye_btn)
        time.sleep(5)
        if eye_btn.is_displayed():
            time.sleep(3)
            assert True
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_btn', attachment_type=AttachmentType.PNG)
            message14 = "Eye button of login page is visible and test-case passed successfully.."
            allure.attach(message14, name="Eye_btn_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name='test_eye_btn', attachment_type=AttachmentType.PNG)
            message15 = "Eye button of login page is not visible and test-case failed.."
            allure.attach(message15, name="Eye_btn_test", attachment_type=allure.attachment_type.TEXT)
            self.driver.close()
            assert False



    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Testing Footer visibility of Login Page")
    def test_footer(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        footer = self.driver.find_element(By.XPATH,'//div[@class="desktop-footer"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",footer)
        time.sleep(5)
        if footer.is_displayed():
            time.sleep(3)
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
    def test_valid_login(self,setup):
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
        act_successful_login = self.driver.find_element(By.ID,self.success_login_id).text
        if act_successful_login == "Update your Profile":
            time.sleep(3)
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



    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Testing Invalid Login of Login Page")
    def test_invalid_login(self, setup):
            self.driver = setup
            self.driver.get(self.page_url)
            time.sleep(3)
            self.driver.maximize_window()
            time.sleep(5)
            self.login_lp = Kotak_Login_Page(self.driver)
            self.login_lp.enter_username(self.invalid_username)
            self.login_lp.enter_password(self.invalid_password)
            self.login_lp.click_login_btn()
            self.driver.maximize_window()
            time.sleep(5)
            error_message = self.driver.find_element(By.XPATH, '//div[@class="mb-2 login-msg"]').text
            if error_message == "Invalid Email Or Password":
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






