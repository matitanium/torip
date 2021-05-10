#modules

import requests
import os
import time








#proxies for request 
data = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
    }

os.system("service tor start")

#loop for requests
while True:
    os.system("service tor start")
    time.sleep(0.5)
    os.system("service tor reload")
    print("new")
    for i in range(8):
        res = requests.get("https://api.ipify.org/",proxies=data).text
        print(res)
    os.system("service tor stop")


