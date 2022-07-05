import time

from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By

class Login:
    def __init__(self):
        self.email = "YOUR_EMAIL" #argparse
        self.password = "YOUR_PASSWORD"#input("Enter password : ") #argparse

    def login(self, base_link, driver):
        driver.get(base_link)
        email_input = driver.find_element(By.ID, "username")
        email_input.click()
        email_input.send_keys(self.email)
        password_input = driver.find_element(By.ID, "password")
        password_input.click()
        password_input.send_keys(self.password)
        sign_in = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
        sign_in.click()
        time.sleep(5)
        feed_page_confirm = driver.find_element(By.CLASS_NAME, "t-16").text
        welcome = "Welcome"
        if welcome not in feed_page_confirm:
            skip = driver.find_element(By.CLASS_NAME, "secondary-action-new")
            skip.click()



        #https: // www.linkedin.com / check / manage - account
