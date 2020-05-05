import time
import pickle

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def dashboard(name):
    chromedriver = "./driver/chromedriver"
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)

    driver.get('https://www.bing.com/')
    time.sleep(2)
    try:
        for bing in pickle.load(open("./cookie/" + name + "/bing.pkl", "rb")):
            if 'expiry' in bing:
                del bing['expiry']
            driver.add_cookie(bing)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.get('https://account.microsoft.com/')
        for microsoft in pickle.load(open("./cookie/" + name + "/microsoft.pkl", "rb")):
            if 'expiry' in microsoft:
                del microsoft['expiry']
            driver.add_cookie(microsoft)
        time.sleep(2)
        driver.get('https://account.microsoft.com/?ref=MeControl')
    except Exception as e:
        print(e)
        driver.quit()
    input("Press Enter to continue...")
    driver.quit()
