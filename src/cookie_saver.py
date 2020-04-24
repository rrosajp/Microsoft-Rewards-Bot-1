import time
import pickle
import os
import argparse
import json
import warnings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def cookie_saver(email, passwd, name, nhd):
    print("Cookie_saver is loading for " + name + "...")

    warnings.filterwarnings("ignore", category=DeprecationWarning)
    chromedriver = "./driver/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    if(nhd==False):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1080x720')
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    driver.get('https://login.live.com')

    try:
        elem = driver.find_element_by_name('loginfmt')
        elem.clear()
        elem.send_keys(email)
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        elem2 = driver.find_element_by_name('passwd')
        elem2.clear()
        elem2.send_keys(passwd)
        elem3 = driver.find_element_by_name('KMSI')
        elem3.click()
        elem2.send_keys(Keys.ENTER)
        time.sleep(5)
        pickle.dump( driver.get_cookies() , open("./cookie/" + name + "/microsoft.pkl","wb"))
        time.sleep(5)
        driver.get('https://www.bing.com')
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        pickle.dump( driver.get_cookies() , open("./cookie/" + name + "/bing.pkl","wb"))
    except Exception as e:
        print(e)
        time.sleep(5)
        time.sleep(5)
        driver.quit()
        time.sleep(2)
    driver.quit()
