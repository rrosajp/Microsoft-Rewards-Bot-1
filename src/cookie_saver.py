import time
import pickle
import os
import argparse
import json
import warnings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException  

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
    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    driver.get('https://login.live.com')
    time.sleep(2)
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
        time.sleep(5)
        if(check_exists_by_xpath("//*[@id='id_s']")):
            driver.find_element_by_xpath("//*[@id='id_s']").click()
            time.sleep(2)
            driver.get('https://www.bing.com')
            time.sleep(2)
            driver.refresh()
            time.sleep(2)
    except Exception as e:
        print(e)
        time.sleep(2)
        driver.quit()
        time.sleep(2)
    driver.quit()
