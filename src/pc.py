import json
import random
import time
import pickle
import os
import warnings

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def pc(name, nhd, num):
    with open("./src/words_list.json") as f:
        data = f.read()
        words_list = random.sample(json.loads(data)['data'], num)
        print('{0} words selected from {1}'.format(len(words_list), "words_list.json"))
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    chromedriver = "./driver/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    if(nhd==False):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1080x720')
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    driver.get('https://account.microsoft.com/')
    time.sleep(5)
    try:
        for microsoft in pickle.load(open("./cookie/" + name + "/microsoft.pkl", "rb")):
            if 'expiry' in microsoft:
                del microsoft['expiry']
            driver.add_cookie(microsoft)
        time.sleep(2)
        driver.refresh()
        time.sleep(5)
        driver.get('https://www.bing.com/')
        for bing in pickle.load(open("./cookie/" + name + "/bing.pkl", "rb")):
            if 'expiry' in bing:
                del bing['expiry']
            driver.add_cookie(bing)
        time.sleep(2)
        driver.refresh()
        time.sleep(5)
    except Exception as e:
        print(e)
        driver.quit()

    url_base = 'http://www.bing.com/search?q='

    for num, word in enumerate(words_list):
        print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
        try:
            driver.get(url_base + word)
            print('\t' + driver.find_element_by_tag_name('h2').text)
        except Exception as e1:
            print(e1)
            time.sleep(2)
    time.sleep(2)
    driver.quit()
