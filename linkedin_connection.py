from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

options = Options()

# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def linkedin_connection(email, password):
    driver.get("https://www.linkedin.com/")
    time.sleep(3)
    driver.find_element_by_id("session_key").send_keys(email)
    driver.find_element_by_name("session_password").send_keys(password)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('/html/body/main/section[1]/div[2]/form/button').click() 
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mynetwork-nav-item"]/a').click()
    time.sleep(6)
    while True:
        buttons = driver.find_elements_by_xpath('//button[@data-control-name="people_connect"]')

        for button in buttons:
            button.click()
            time.sleep(1)
        
        driver.refresh()


linkedin_connection("EMAIL OR PHONE", "PASSWORD")