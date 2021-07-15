from selenium import webdriver as wd
import glv
import dbg
import time
import traceback
import random

import chromedriver_binary

dbg = dbg.dbgr()

class bestbuy:
    username = None
    password = None
    firstname = None
    lastname = None
    address = None
    city = None
    state = None
    zipcode = None
    card = None
    expmonth = None
    expyear = None
    cvv = None
    pn = None
    driver = None
    dbgr = None

    def __init__(self):
        self.driver = wd.Chrome()
        self.driver.implicitly_wait(5)

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
        self.username = userdata[0]
        self.password = userdata[1]
        self.firstname = userdata[2]
        self.lastname = userdata[3]
        self.address = userdata[4]
        self.city = userdata[5]
        self.state = userdata[6]
        self.zipcode = userdata[7]
        self.card = userdata[8]
        self.expmonth = userdata[9]
        self.expyear = userdata[10]
        self.cvv = userdata[11]
        self.pn = userdata[12]
    
    def purchase(self, link):
        self.driver.get(link)
        
        dbg.debug("Starting Program")
        try:
            #add to cart
            self.attempt(self.addToCart)

            #checkout
            self.attempt(self.checkout)

            #Login
            self.attempt(self.login)

            #Enter Shipping Info
            self.attempt(self.shippingInfo)

            #Enter Payment Info
            self.attempt(self.paymentInfo)

        except:
            dbg.debug("Program failed: " + traceback.format_exc())
            dbg.crash(self.driver.page_source)
            self.driver.close

    def attempt(self, func):
        running = True
        curAttempt = 0
        while(running):
            try:
                func()
                running = False
            except:
                curAttempt += 1
                if(curAttempt > glv.MAX_RETRYS_PER_TASK):
                    raise
                else:
                    dbg.debug("Current task failed, refreshing and retrying")
                    self.driver.refresh()
    
    def addToCart(self):
        dbg.debug("---Adding To Cart:")

        current_button = self.driver.find_element_by_class_name("add-to-cart-button")
        dbg.debug("Found add-to-cart button")

        while(current_button.get_attribute("data-button-state")) == "SOLD_OUT":
            dbg.debug("item is sold out, retrying in 10")
            time.sleep(random.randint(glv.MIN_REFRESH_TIME,glv.MAX_REFRESH_TIME))
            self.driver.refresh
            continue
        
        #Clicks the add-cart button
        dbg.debug("Clicking the add-to-cart button")
        current_button.click()

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        inqueue = True
        seconds = 0
        while(inqueue):
            if(current_button.get_attribute("data-button-state")) != "ADD_TO_CART":
                dbg.debug("Waiting in queue for {seconds} seconds")
                time.sleep(0.5)
                seconds += 0.5
            else:
                #Clicks the add-cart button
                current_button.click()
                dbg.debug("Attempting to add to cart")
                inqueue = False

        #Clicks the go-to-cart button
        dbg.debug("Clicking 'Go To Cart'")
        current_button = self.driver.find_element_by_class_name("c-button-block")
        current_button.click()

        #check for next elenement before continuing

    def checkout(self):
        dbg.debug("---Checkout:")

        #Clicks the checkout button
        dbg.debug("Clicking 'Checkout'")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

        #check for next elenement before continuing

    def login(self):
        if glv.GUEST:
            dbg.debug("---Login: (as guest)")

            #Clicks login
            dbg.debug("Clicking the 'login as guest' button")
            current_button = self.driver.find_element_by_class_name("cia-guest-content__continue")
            current_button.click()
        else:
            dbg.debug("---Login: (as user)")

            #Enter Username 
            dbg.debug("Entering Email Address")
            current_button = self.driver.find_element_by_id("fld-e")
            current_button.send_keys(self.username)

            #Enter Password
            dbg.debug("Entering Password")
            current_button = self.driver.find_element_by_id("fld-p1")
            current_button.send_keys(self.password)

            #Clicks login
            dbg.debug("Clicking the login button")
            current_button = self.driver.find_element_by_class_name("cia-form__controls__submit")
            current_button.click()


    def shippingInfo(self):
        dbg.debug("---Shipping Info:")
        #Enters Firstname
        dbg.debug("Entering Firstname")
        current_button = self.driver.find_element_by_css_selector('input[id$=firstName]')
        current_button.send_keys(self.firstname)
        
        #Enters Lastname
        dbg.debug("Entering Lastname")
        current_button = self.driver.find_element_by_css_selector('input[id$=lastName]')
        current_button.send_keys(self.lastname)
        
        #Enters Address
        dbg.debug("Entering Address")
        current_button = self.driver.find_element_by_css_selector('input[id$=street]')
        current_button.send_keys(self.address)
        
        #Enters City
        dbg.debug("Entering City")
        current_button = self.driver.find_element_by_css_selector('input[id$=city]')
        current_button.send_keys(self.city)
        
        #Enters State
        dbg.debug("Entering State")
        current_button = self.driver.find_element_by_name("state") #wont find with css for some reason
        current_button.send_keys(self.state)
        
        #Enters Zipcode
        dbg.debug("Entering Zipcode")
        current_button = self.driver.find_element_by_css_selector('input[id$=zipcode]')
        current_button.send_keys(self.zipcode)

        if glv.GUEST:
            dbg.debug("Entering Email")
            current_button = self.driver.find_element_by_id("user.emailAddress")
            current_button.send_keys(self.username)

            dbg.debug("Entering Phone Number")
            current_button = self.driver.find_element_by_id("user.phone")
            current_button.send_keys(self.pn)
        
        #Clicks 'Continue to Payment Information'
        dbg.debug("Clicking 'Continue to Payment Information'")
        current_button = self.driver.find_element_by_class_name("btn-secondary")
        current_button.click()

        #check for next elenement before continuing

    def paymentInfo(self):
        dbg.debug("---Payment Info:")
        
        #Enter Credit Card information
        dbg.debug("Entering Card Number")
        current_button = self.driver.find_element_by_id("optimized-cc-card-number")
        current_button.send_keys(self.card)
        
        #Enter Month
        dbg.debug("Entering Month")
        current_button = self.driver.find_element_by_name("expiration-month")
        current_button.send_keys(self.expmonth)
        
        #Enter Year
        dbg.debug("Entering Year")
        current_button = self.driver.find_element_by_name("expiration-year")
        current_button.send_keys(self.expyear)
        
        #Enter CCV
        dbg.debug("Entering CCV")
        current_button = self.driver.find_element_by_id("credit-card-cvv")
        current_button.send_keys(self.cvv)

        #check for next element before continuing
    
    def buyItem(self):        
        #place order
        dbg.debug("Clicking 'Purchase'")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

        #TODO check for success/failure. return True on success, False for failure
        return True

    def close(self):
        self.driver.close
        

