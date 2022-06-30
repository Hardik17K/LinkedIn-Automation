from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from login import Login
from search import Search
from webdriver_manager.chrome import ChromeDriverManager

login = Login()
search = Search()
base_link = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get(base_link)
driver.maximize_window()


#print(email_input)

login.login(base_link, driver)
search.search(driver)
search.filter(driver)

