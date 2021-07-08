from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg
import time
import traceback
import chromedriver_binary # type: ignore

#Initialize debugger
dbgr = dbg.dbgr()

#Parse user-details.txt
lines = []
userdata = []
with open("user-details.txt", "r") as f:
    lines = f.readlines()

count = 0
for line in lines:
    linestr = line.split('=')
    userdata.append(linestr[1])
    count += 1

#User-details
username = userdata[0]
password = userdata[1]
firstname = userdata[2]
lastname = userdata[3]
address = userdata[4]
city = userdata[5]
state = userdata[6]
zipcode = userdata[7]
card = userdata[8]
expmonth = userdata[9]
expyear = userdata[10]
cvv = userdata[11]

#initialize webdriver
wd = wd.Chrome()
wd.implicitly_wait(10) 

#Item list
#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
wd.get("https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286") #test-item (in-stock)

running = True
while running:
    dbgr.debug("Starting Program")
    try:
        time.sleep(3)
        wd.refresh()
        cartbutton = wd.find_element_by_class_name("add-to-cart-button")

        dbgr.debug("Found add-to-cart button")

        if(cartbutton.get_attribute("data-button-state")) == "SOLD_OUT":
            dbgr.debug("item is sold out, retrying in 10")
            continue
        
        dbgr.debug("item is not sold out, trying to add to cart")
        
        #Clicks the add-cart button
        dbgr.debug("Clicking the add-to-cart button")
        cartbutton.click()

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        inqueue = True
        seconds = 0
        while(inqueue):
            if(cartbutton.get_attribute("data-button-state")) != "ADD_TO_CART":
                dbgr.debug("Waiting in queue for {seconds} seconds")
                time.sleep(0.5)
                seconds += 0.5
            else:
                 #Clicks the add-cart button
                cartbutton.click()
                dbgr.debug("Attempting to add to cart")
                inqueue = False

        #Clicks the go-to-cart button
        dbgr.debug("Clicking the go-to-cart button")
        cartbutton = wd.find_element_by_class_name("c-button-block")
        cartbutton.click()

        #Clicks the checkout button
        dbgr.debug("Clicking the checkout button")
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()

        #Enter Username 
        dbgr.debug("Entering Username")
        cartbutton = wd.find_element_by_id("fld-e")
        cartbutton.send_keys(username)
        

        #Enter Password
        dbgr.debug("Entering Password")
        cartbutton = wd.find_element_by_id("fld-p1")
        cartbutton.send_keys(password)

        #Clicks login
        dbgr.debug("Clicking the login button")
        cartbutton = wd.find_element_by_class_name("cia-form__controls__submit")
        cartbutton.click()

        #Enters Firstname
        dbgr.debug("Entering Firstname")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.firstName")
        cartbutton.send_keys(firstname)

        #Enters Lastname
        dbgr.debug("Entering Lastname")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.lastName")
        cartbutton.send_keys(lastname)

        #Enters Address
        dbgr.debug("Entering Address")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.street")
        cartbutton.send_keys(address)

        #Enters City
        dbgr.debug("Entering City")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.city")
        cartbutton.send_keys(city)

        #Enters State
        dbgr.debug("Entering State")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.state")
        cartbutton.send_keys(state)

        #Enters Zipcode
        dbgr.debug("Entering Zipcode")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.zipcode")
        cartbutton.send_keys(zipcode)

        #Clicks 'Continue to Payment Information'
        dbgr.debug("Clicking 'Continue to Payment Information'")
        cartbutton = wd.find_element_by_class_name("btn-secondary")
        cartbutton.click()

        #Enter Credit Card information
        dbgr.debug("Entering Card Number")
        cartbutton = wd.find_element_by_id("optimized-cc-card-number")
        cartbutton.send_keys(card)

        #Enter Month
        dbgr.debug("Entering Month")
        cartbutton = wd.find_element_by_name("expiration-month")
        cartbutton.send_keys(expmonth)

        #Enter Year
        dbgr.debug("Entering Year")
        cartbutton = wd.find_element_by_name("expiration-year")
        cartbutton.send_keys(expyear)

        #Enter CCV
        dbgr.debug("Entering CCV")
        cartbutton = wd.find_element_by_id("credit-card-cvv")
        cartbutton.send_keys(cvv)

        #place order
        dbgr.debug("Clicks Purchase")
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()

        wd.close
        break
    except:
        dbgr.debug("Program failed: " + traceback.format_exc())
        wd.close
        break




