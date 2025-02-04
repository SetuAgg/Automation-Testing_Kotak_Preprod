from selenium.webdriver.common.by import By


class Kotak_Dashboard_page_Detailed:
    view_more_btn = "//button[text()='View More']"

    def __init__(self, driver):
        self.driver = driver

    def click_view_more_btn(self):
        self.driver.find_element(By.XPATH,self.view_more_btn).click()





