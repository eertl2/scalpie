from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg
import bestbuy
import chromedriver_binary # type: ignore

#Initialize debugger
dbgr = dbg.dbgr()

#Item list
#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
item = "https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286" #test-item (in-stock)

running = True
while running:
    bb = bestbuy.bestbuy()
    bb.purchase(item)
    running = False