from selenium.webdriver.common.by import By


class Kotak_Login_Page:
    textbox_username_name = "email"
    textbox_password_id = "passInput"
    btn_login_xpath = '//button[@type="submit"]'
    btn_forgot_xpath = "//a[text()='Forgot Password?']"
    eye_btn = '//div[@class="show-password"]'
    close_btn_forgot_pass = '//button[@class="btn-close"]'
    profile_dropdown = '//div[@class="step1"]'
    logout= "//a[text()='Log out']"


    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)


    def click_login_btn(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_forgot_password_btn(self):
        self.driver.find_element(By.XPATH,self.btn_forgot_xpath).click()

    def click_eye_btn(self):
        self.driver.find_element(By.XPATH,self.eye_btn).click()

    def click_close_btn(self):
        self.driver.find_element(By.XPATH,self.close_btn_forgot_pass).click()

    def click_profile_dropdown(self):
        self.driver.find_element(By.XPATH,self.profile_dropdown).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout).click()





