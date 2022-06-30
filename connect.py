import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Connect:
    def __init__(self):
        self.intensity = int(input("What intensity to run : "))

    def company(self, driver):
        wait = WebDriverWait(driver, 20)
        print("I m in")
        i=1
        n=1
        while i <= self.intensity:
            follow_button = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{i}]/div/div/div[3]/div/button')))
            if follow_button.get_attribute('aria-label') == 'Following':
                self.intensity = self.intensity+1
            else:
                follow_button.click()
                company_name = driver.find_element(By.XPATH, f'/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{i}]/div/div/div[2]/div[1]/div[1]/div/span/span/a').text
                print("following "+ company_name)
            i+=1
            if(i>10 and i <= self.intensity):
                n += 1
                body = driver.find_element_by_css_selector('body')
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[4]/div/div/ul/li[{n}]/button'))).click()
                i=1
                self.intensity = 1
            print(i)


    def people(self, driver):
        wait = WebDriverWait(driver, 20)
        print("I m in")
        i = 1
        n = 1
        self.intensity = 3*self.intensity + 1
        x = 1
        while x <= self.intensity:
            print(i)
            time.sleep(2)
            try:
                connect_button = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{i}]/div/div/div[3]/div/button')))
            except:
                self.intensity = self.intensity + 1
                i = i+1
                x = x+1
                if i > 10 and x <= self.intensity:
                    n += 1
                    body = driver.find_element_by_css_selector('body')
                    body.send_keys(Keys.PAGE_DOWN)
                    body.send_keys(Keys.PAGE_DOWN)
                    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[aria-label='Page {n}']"))).click()
                    i = 1
                continue
            print(connect_button.text)
            if connect_button.text == 'Connect':
                wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{i}]/div/div/div[3]/div/button'))).click()
                #/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[3]/div/button
                wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')))
                popup = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
                print(popup.is_enabled())
                if popup.is_enabled():
                    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]'))).click()
                    #/html/body/div[3]/div/div/div[3]/button[2]
                else:
                    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/button/li-icon'))).click()

                name = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div/ul/li[{i}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                print("Connection requested to " + name)
            elif connect_button.text == 'Follow':
                connect_button.click()
                name = driver.find_element(By.XPATH, f'/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div/ul/li[{i}]/div/div/div[2]/div[1]/div[1]/div/span[1]/span/a/span/span[1]').text
                print("Following " + name)
            else:
                self.intensity = self.intensity + 1

            i += 1
            x += 1

            if i > 10 and x <= self.intensity:
                n += 1
                body = driver.find_element_by_css_selector('body')
                body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.PAGE_DOWN)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[aria-label='Page {n}']"))).click()
                i = 1

#/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul
#/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/ul/li[2]/div/div/div[2]/div[1]/div[1]/div/span/span/a/text()
#/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul
##/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div/ul/li[1]/div/div/div[3]/div/button
#/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[2]/div[1]/div[1]/div

#/html#/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[{i}]/div/div/div[3]/div/button
#/html#/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[3]/div/button
#/html/body/div[6]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/ul/li[1]/div/div/div[3]/div/button