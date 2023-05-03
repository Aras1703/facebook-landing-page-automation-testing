import facebook.constants as const
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Facebook(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(Facebook, self).__init__(service=Service(ChromeDriverManager().install()),
                                       options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown == True:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def put_email(self, email_phone):
        email_field = self.find_element(By.ID, "email")
        email_field.click()
        email_field.send_keys(email_phone)

    def put_password(self, password):
        pass_field = self.find_element(By.ID, "pass")
        pass_field.click()
        pass_field.send_keys(password)
    
    def view_password(self):
        view_pass = self.find_element(By.CLASS_NAME, "_9lsa")
        view_pass.click()
        self.execute_script(view_pass)

    def press_login(self):
        hit_login = self.find_element(By.NAME, "login").click()
        self.execute_script(hit_login)
    
    def forgot_password(self):
        restore_password = self.find_elements(By.XPATH, "//div[@class='_6ltj']//a[@href]")
        for restore in restore_password:
            restore.click()
            self.execute_script(restore)

    def create_account(self):
        new_accounts = self.find_elements(By.XPATH, "//div[@class='_6ltg']//a[@class]")
        for new_account in new_accounts:
            new_account.click()
            self.execute_script(new_account)

    def create_pages(self):
        new_pages = self.find_element(By.CLASS_NAME, "_8esh")
        new_pages.click()
        self.execute_script(new_pages)
