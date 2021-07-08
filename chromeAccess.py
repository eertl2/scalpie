from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import dbg
import time
import chromedriver_binary # type: ignore

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

wd = wd.Chrome()
wd.implicitly_wait(10) 

#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
wd.get("https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286") #test-item (in-stock)

running = True
#success = False

while running:
    dbg.debug("Starting Program")
    try:
        time.sleep(3)
        wd.refresh()
        cartbutton = wd.find_element_by_class_name("add-to-cart-button")

        dbg.debug("Found add-to-cart button")

        if(cartbutton.get_attribute("data-button-state")) == "SOLD_OUT":
            dbg.debug("item is sold out, retrying in 10")
            continue
        
        dbg.debug("item is not sold out, trying to add to cart")
        
        #Clicks the add-cart button
        dbg.debug("Clicking the add-to-cart button")
        cartbutton.click()

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        inqueue = True
        seconds = 0
        while(inqueue):
            if(cartbutton.get_attribute("data-button-state")) != "ADD_TO_CART":
                dbg.debug("Waiting in queue for {seconds} seconds")
                time.sleep(0.5)
                seconds += 0.5
            else:
                 #Clicks the add-cart button
                cartbutton.click()
                dbg.debug("Attempting to add to cart")
                inqueue = False

        #Clicks the go-to-cart button
        dbg.debug("Clicking the go-to-cart button")
        cartbutton = wd.find_element_by_class_name("c-button-block")
        cartbutton.click()

        #Clicks the checkout button
        dbg.debug("Clicking the checkout button")
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()

        #Enter Username 
        dbg.debug("Entering Username")
        cartbutton = wd.find_element_by_id("fld-e")
        cartbutton.send_keys(username)
        

        #Enter Password
        dbg.debug("Entering Password")
        cartbutton = wd.find_element_by_id("fld-p1")
        cartbutton.send_keys(password)

        #Clicks login
        dbg.debug("Clicking the login button")
        cartbutton = wd.find_element_by_class_name("cia-form__controls__submit")
        cartbutton.click()

        #Enters Firstname
        dbg.debug("Entering Firstname")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.firstName")
        cartbutton.send_keys(firstname)

        #Enters Lastname
        dbg.debug("Entering Lastname")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.lastName")
        cartbutton.send_keys(lastname)

        #Enters Address
        dbg.debug("Entering Address")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.street")
        cartbutton.send_keys(address)

        #Enters City
        dbg.debug("Entering City")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.city")
        cartbutton.send_keys(city)

        #Enters State
        dbg.debug("Entering State")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.state")
        cartbutton.send_keys(state)

        #Enters Zipcode
        dbg.debug("Entering Zipcode")
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.zipcode")
        cartbutton.send_keys(zipcode)

        #Clicks 'Continue to Payment Information'
        dbg.debug("Clicking 'Continue to Payment Information'")
        cartbutton = wd.find_element_by_class_name("btn-secondary")
        cartbutton.click()

        #Enter Credit Card information
        dbg.debug("Entering Card Number")
        cartbutton = wd.find_element_by_id("optimized-cc-card-number")
        cartbutton.send_keys(card)

        #Enter Month
        dbg.debug("Entering Month")
        cartbutton = wd.find_element_by_name("expiration-month")
        cartbutton.send_keys(expmonth)

        #Enter Year
        dbg.debug("Entering Year")
        cartbutton = wd.find_element_by_name("expiration-year")
        cartbutton.send_keys(expyear)

        #Enter CCV
        dbg.debug("Entering CCV")
        cartbutton = wd.find_element_by_id("credit-card-cvv")
        cartbutton.send_keys(cvv)

        #place order
        dbg.debug("Clicks Purchase")
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()

        wd.close
        break
    except:
        print("Program failed")
        wd.close
        break




