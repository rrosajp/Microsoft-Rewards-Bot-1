import json
import random
import time
import pickle
import os
import warnings

import requests
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def mobile(name, nhd, num):
    with open("./src/words_list.json") as f:
        data = f.read()
        words_list = random.sample(json.loads(data)['data'], num)
        print('{0} words selected from {1}'.format(len(words_list), "word_list.json"))
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    chrome_options = Options()
    mobile_emulation = { "deviceName": "Galaxy S5" } #Specifying device
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--auto-open-devtools-for-tabs")
    if(nhd==False):
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1080x720')
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation) #For mobile
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    if(platform == "linux" or platform == "linux2" or platform == "linux3"):
        chromedriver = "./driver/chromedriver_linux"
    elif(platform == "darwin"):
        chromedriver = "./driver/chromedriver_mac"
    elif(platform == "win32"):
        chromedriver = "./driver/chromedriver_win.exe"
    else:
        print("Your os is not compatible with MS Rewards Bot")
        exit()
        
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    driver.get('https://account.microsoft.com/')
    time.sleep(2)
    try:
        for microsoft in pickle.load(open("./cookie/" + name + "/microsoft.pkl", "rb")):
            if 'expiry' in microsoft:
                del microsoft['expiry']
            driver.add_cookie(microsoft)
        time.sleep(2)
        driver.get('https://account.microsoft.com/?ref=MeControl')
        time.sleep(2)
        driver.get('https://www.bing.com/')
        for bing in pickle.load(open("./cookie/" + name + "/bing.pkl", "rb")):
            if 'expiry' in bing:
                del bing['expiry']
            driver.add_cookie(bing)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
    except Exception as e:
        print(e)
        driver.quit()

    url_base = 'http://www.bing.com/search?q='

    time.sleep(5)

    for num, word in enumerate(words_list):
        print('{0}. URL : {1}'.format(str(num + 1), url_base + word))
        try:
            driver.get(url_base + word)
            print('\t' + driver.find_element_by_tag_name('h2').text)
        except Exception as e1:
            print(e1)
            time.sleep(2)
    driver.quit()
