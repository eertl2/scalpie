from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg
from worker import worker
import threading
import chromedriver_binary

#Item list
#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
item = "https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286" #test-item (in-stock)

threads = []
for i in range(1):
    t = threading.Thread(target=worker, args = ("bestbuy", item))
    threads.append(t)
    t.start()
    
   
