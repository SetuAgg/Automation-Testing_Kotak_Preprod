import pytest
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
            self.driver.save_screenshot(".\\screenshots\\test_title.png")
            self.driver.close()
        else:
            time.sleep(3)
            self.driver.save_screenshot(".\\screenshots\\test_title.png")
            self.driver.close()
            assert False


    def test_welcome_text(self,setup):
        self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        act_welcome_txt = self.driver.find_element(By.XPATH,'//p[@class="welcome_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",act_welcome_txt)
        time.sleep(5)
        assert act_welcome_txt == "Kotak RM Academy",f"Expected welcome text to be 'Kotak RM Academy' but got {act_welcome_txt}"
        time.sleep(5)
        self.driver.save_screenshot(".\\screenshots\\test_welcome_text.png")
        self.driver.close()


    def test_login_text_visible(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        act_login_text = self.driver.find_element(By.XPATH,'//div[@class="login_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",act_login_text)
        time.sleep(5)
        if act_login_text == "LOGIN":
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_login_text.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login_text.png")
            self.driver.close()
            assert False

    def test_forgot_password_text(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        act_forgot_password_text = self.driver.find_element(By.XPATH,'//div[@class="forgot_password_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",act_forgot_password_text)
        time.sleep(5)
        if act_forgot_password_text == "Forgot Password?":
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_forgot_password_text.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_forgot_password_text.png")
            self.driver.close()
            assert False

    def test_forgot_btn_click(self,setup):
        self.driver = setup
        self.driver.get(self.page_url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(5)
        self.login_lp = Kotak_Login_Page(self.driver)
        self.login_lp.click_forgot_password_btn()
        act_success_text = self.driver.find_element(By.XPATH,'//p[@class="reset_paswd_text"]')
        self.driver.execute_script("arguments[0].style.border='5px solid red'",act_success_text)
        time.sleep(5)
        if act_success_text == ("Lost your password? Please enter your Email Address, "
                                "a link will be sent to reset your password."):
            time.sleep(3)
            assert True
            self.driver.save_screenshot(".\\screenshots\\test_forgot_btn_click.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_forgot_btn_click.png")
            self.driver.close()
            assert False

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
            self.driver.save_screenshot(".\\screenshots\\test_logo.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_logo.png")
            self.driver.close()
            assert False

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
            self.driver.save_screenshot(".\\screenshots\\test_image.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_image.png")
            self.driver.close()
            assert False

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
            self.driver.save_screenshot(".\\screenshots\\test_eye_btn.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_eye_btn.png")
            self.driver.close()
            assert False

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
            self.driver.save_screenshot(".\\screenshots\\test_footer.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_footer.png")
            self.driver.close()
            assert False

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
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.driver.close()
            assert False

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
                self.driver.execute_script("arguments[0].style.border='5px solid red'",error_message)
                time.sleep(5)
                assert True
                self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
                self.driver.close()
                assert False






