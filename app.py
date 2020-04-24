import time
import os
import json
import argparse

from src.cookie_saver import cookie_saver
from src.mobile import mobile
from src.pc import pc
from src.dashboard import dashboard

parser = argparse.ArgumentParser(description='Microsoft rewards bot.')
parser.add_argument('-nhd', action='store_true', dest='nhd_stt', default=False, help='Disable headless mode')

args = parser.parse_args()
nhd = args.nhd_stt

def getJSON(file):
    with open(file, 'r') as fp:
        return json.load(fp)

app = getJSON('./passwd.json')
accounts = app["accounts"]

for i in enumerate(accounts):
    data = str(i[1]).replace("\'", "\"")
    x = json.loads(data)
    name = x["name"]
    email = x["email"]
    passwd = x["passwd"]
    
    try:
        os.mkdir("./cookie")
    except Exception:
        print("Cookie folder already exist...")
    try:
        os.mkdir("./cookie/" + name)
    except Exception:
        print("Cookie folder for " + name + " already exist...")
    try:
        os.remove("./cookie/" + name + "/bing.pkl")
    except Exception:
        print("Bing cookie for " + name +" doesn't exist...")
    try:
        os.remove("./cookie/" + name + "/microsoft.pkl")
    except Exception:
        print("Microsoft cookie for " + name +" doesn't exist...")

    cookie_saver(email, passwd, name, nhd)
    mobile(name, nhd, 20)
    pc(name, nhd, 30)

time.sleep(3)

def dash():
    print("Do you want to show dashboard for:")
    res = []
    for i in enumerate(accounts):
        data1 = str(i[1]).replace("\'", "\"")
        x1 = json.loads(data1)
        id = x1["id"]
        name1 = x1["name"]
        email1 = x1["email"]
        passwd1 = x1["passwd"]
        print("  " + name1 + " [" + str(id) + "]")
        res.append(name1)
    print("or exit [E/e]")
    q = input(">>> ")
    try:
        choosen = res[int(q)-1]
        print("Your choice is " + choosen)
        dashboard(choosen)
        dash()
    except Exception:
        if(q == "e" or q == "E"):
            exit()
        else:
            print("Error.. Trying one more time...")
            dash()
dash()
