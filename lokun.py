#coding: utf-8

import time
import sys

import requests
from blink1 import Blink1

# IP?
API = "https://api.lokun.is"

def rgb(status):
    if status.lower() == "red":
        return [255, 0, 0]
    if status.lower() == "yellow":
        return [232, 181, 0]
    if status.lower() == "green":
        #return [0, 255, 0]
        return [0, 0, 0]
    if status.lower() == "blue":
        return [0, 0, 255]

    return rgb("blue")

def get_status():
    try:
        json = requests.get(API + "/lokun/status", timeout=4.20).json()
        return json["status"]
    except IndexError:
        return "red"
    except Exception as ex:
        try:
            requests.get("http://google.com", timeout=4.20)
        except Exception:
            return "blue"
        return "red"

def clear(blink1):
    blink1.fade_to_rgb(200, 0, 0, 0)
    time.sleep(0.2)

def set_color(blink1, status, flash=False):
    r, g, b = rgb(status)

    if flash:
        clear(blink1)
        blink1.fade_to_rgb(200, r, g, b)
        time.sleep(0.1)
        clear(blink1)

    else:
        blink1.fade_to_rgb(200, r, g, b)

def main(color=""):
    status = color or get_status()
    print "Status: " + status
    blink1 = Blink1()
    set_color(blink1, status)
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
    
