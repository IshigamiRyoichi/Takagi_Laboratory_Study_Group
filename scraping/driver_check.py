from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time

def set_up_chrome_driver():
    options = Options() 
    chrome_driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
    return chrome_driver

def move_on_google_home(chrome_driver):
    chrome_driver.get("https://www.yahoo.co.jp/")
    time.sleep(0.5)
    
if __name__=='__main__':
    chrome_driver = set_up_chrome_driver()
    move_on_google_home(chrome_driver)
    chrome_driver.quit()