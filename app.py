import time
import os
import json
import argparse
import re
import sys
from signal import signal, SIGINT

from src.cookie_saver import cookie_saver
from src.mobile import mobile
from src.pc import pc
from src.dashboard import dashboard

parser = argparse.ArgumentParser(description='Microsoft rewards bot.')
parser.add_argument('-nhd', action='store_true', dest='nhd_stt', default=False, help='Disable headless mode')

args = parser.parse_args()
nhd = args.nhd_stt

def clear(num):
    for i in range(num):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

def handler(ln, err):
     clear(1)
     print("Good Bye !!")
     sys.exit(0)

signal(SIGINT, handler)

def getJSON(file):
    if(os.path.exists("passwd.json")):
        try:
            with open(file, 'r') as fp:
                return json.load(fp)
        except Exception as e:
            print("Your passwd.json as bad format")
            exit()
    else:
        print("Please create a passwd.json")
        exit()
        
app = getJSON('./passwd.json')
accounts = app["accounts"]

for i in enumerate(accounts):
    data = str(i[1]).replace("\'", "\"")
    x = json.loads(data)
    name = x["name"]
    email = x["email"]
    passwd = x["passwd"]

    if not(os.path.exists("cookie")):
        os.mkdir("cookie")
    if not(os.path.exists(os.path.join("cookie", name))):
        os.mkdir(os.path.join("cookie", name))
    if(os.path.exists(os.path.join("cookie", name, "bing.pkl"))):
        os.remove(os.path.join("cookie", name, "bing.pkl"))
    if(os.path.exists(os.path.join("cookie", name, "microsoft.pkl"))):
        os.remove(os.path.join("cookie", name, "microsoft.pkl"))

    cookie_saver(email, passwd, name, nhd)
    mobile(name, nhd, 22)
    pc(name, nhd, 32)

time.sleep(3)

def dash():
    print("Do you want to show dashboard for:")
    res = []
    acc = 0
    for i in enumerate(accounts):
        acc += 1
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
    if(re.match("\d", q)):
        if(int(q)<=acc and int(q)>=1):
            choosen = res[int(q)-1]
            print("Your choice is " + choosen)
            dashboard(choosen)
            dash()
        else:
            print("Error.. Trying one more time...")
            dash()
    elif(q == "e" or q == "E"):
        exit()
    else:
        print("Error.. Trying one more time...")
        dash()
dash()
