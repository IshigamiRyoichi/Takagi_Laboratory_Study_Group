from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import time
import json

def set_up_chrome_driver():
    options = Options() 
    chrome_driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
    return chrome_driver

def login_moodel(chrome_driver,id,pswd):
    chrome_driver.get("https://kadai-moodle.kagawa-u.ac.jp/login/index.php")
    chrome_driver.find_element_by_name("username").send_keys(id)
    time.sleep(0.5)
    chrome_driver.find_element_by_name("password").send_keys(pswd)
    time.sleep(0.5)
    chrome_driver.find_elements_by_id('loginbtn')[0].click()
    time.sleep(0.5)

def get_list_a_tag_href(chrome_driver):
    chrome_driver.get("https://kadai-moodle.kagawa-u.ac.jp/my/")
    html_data = chrome_driver.page_source.encode("utf-8")
    soup = BeautifulSoup(html_data, 'html.parser')
    elems = soup.select('a')
    href_list = []
    for elem in elems:
        href = elem.get('href')
        href_list.append(href)
    print(href_list)
    
if __name__=='__main__':
    open_json = open('./json/login.json','r')
    session = json.load(open_json)
    id=session['id']
    pswd=session['pswd']
    chrome_driver = set_up_chrome_driver()
    login_moodel(chrome_driver,id,pswd)
    get_list_a_tag_href(chrome_driver)

    chrome_driver.quit()