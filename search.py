from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from connect import Connect


connect = Connect()


class Search:
    def __init__(self):
        self.final_filter_text = None
        self.search_text = input("What to search about : ") #argparse
        self.filter_by = input("Filter type : ")



    def search(self, driver):
        wait = WebDriverWait(driver, 200)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=Search]"))).click()
        search_input = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
        search_input.send_keys(self.search_text)
        search_input.send_keys(Keys.ENTER)

    def filter(self, driver):
        wait = WebDriverWait(driver, 10)
        self.filter_by = self.filter_by.upper()
        company = ["COMPANY", "COMPANIES", "COMPANIE"]
        people = ["PEOPLE"]
        time.sleep(5)
        if self.filter_by in company:
            self.filter_by = "Companies"
        #print(self.filter_by)
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[7]/button').click()
            connect.company(driver)

        elif self.filter_by in people:
            self.filter_by = "People"
        #print(self.filter_by)
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div[2]/section/div/nav/div/ul/li[1]/button'))).click()
            connect.people(driver)
        self.final_filter_text = self.filter_by
        time.sleep(20)









