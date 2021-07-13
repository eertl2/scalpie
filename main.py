from selenium import webdriver as wd
#from selenium.webdriver.support import expected_conditions as EC
#import glv
#import dbg
#from threading import Lock
from worker import worker
from threading import Lock
import threading
import chromedriver_binary

threads = []
for i in range(2):
    t = threading.Thread(target=worker, args = ("bestbuy", glv.ITEM))
    threads.append(t)
    t.start()
    
   
