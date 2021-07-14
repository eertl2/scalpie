from selenium import webdriver as wd
import glv
import dbg
import time
import traceback
import random
from purchasing import purchasing

import chromedriver_binary

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
        self.dbgr = dbg.dbgr()

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
        
        running = True
        while running:
            self.dbgr.debug("Starting Program")
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

                # #Purchase
                # if(self.buyItem()):
                #     self.driver.close
                #     return True
                self.driver.close

                return True
            except:
                self.dbgr.debug("Program failed: " + traceback.format_exc())
                self.dbgr.crash(self.driver.page_source)
                self.driver.close
                return False

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
                    self.dbgr.debug("Current task failed, refreshing and retrying")
                    self.driver.refresh()
    
    def addToCart(self):
        self.dbgr.debug("---Adding To Cart:")

        current_button = self.driver.find_element_by_class_name("add-to-cart-button")
        self.dbgr.debug("Found add-to-cart button")

        while(current_button.get_attribute("data-button-state")) == "SOLD_OUT":
            self.dbgr.debug("item is sold out, retrying in 10")
            time.sleep(random.randint(glv.MIN_REFRESH_TIME,glv.MAX_REFRESH_TIME))
            self.driver.refresh
            continue
        
        #Clicks the add-cart button
        #self.dbgr.debug("Clicking the add-to-cart button")
        #current_button.click()

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        inqueue = True
        seconds = 0
        while(inqueue):
            if(current_button.get_attribute("data-button-state")) != "ADD_TO_CART":
                self.dbgr.debug("Waiting in queue for {seconds} seconds")
                time.sleep(0.5)
                seconds += 0.5
            else:
                #Clicks the add-cart button
                current_button.click()
                self.dbgr.debug("Attempting to add to cart")
                inqueue = False

        #Clicks the go-to-cart button
        self.dbgr.debug("Clicking 'Go To Cart'")
        current_button = self.driver.find_element_by_class_name("c-button-block")
        current_button.click()

        #check for next elenement before continuing

    def checkout(self):
        self.dbgr.debug("---Checkout:")

        #Clicks the checkout button
        self.dbgr.debug("Clicking 'Checkout'")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

        #check for next elenement before continuing

    def login(self):
        if glv.GUEST:
            self.dbgr.debug("---Login: (as guest)")

            #Clicks login
            self.dbgr.debug("Clicking the 'login as guest' button")
            current_button = self.driver.find_element_by_class_name("cia-guest-content__continue")
            current_button.click()
        else:
            self.dbgr.debug("---Login: (as user)")

            #Enter Username 
            self.dbgr.debug("Entering Email Address")
            current_button = self.driver.find_element_by_id("fld-e")
            current_button.send_keys(self.username)

            #Enter Password
            self.dbgr.debug("Entering Password")
            current_button = self.driver.find_element_by_id("fld-p1")
            current_button.send_keys(self.password)

            #Clicks login
            self.dbgr.debug("Clicking the login button")
            current_button = self.driver.find_element_by_class_name("cia-form__controls__submit")
            current_button.click()


    def shippingInfo(self):
        self.dbgr.debug("---Shipping Info:")
        #Enters Firstname
        self.dbgr.debug("Entering Firstname")
        current_button = self.driver.find_element_by_css_selector('input[id$=firstName]')
        current_button.send_keys(self.firstname)
        
        #Enters Lastname
        self.dbgr.debug("Entering Lastname")
        current_button = self.driver.find_element_by_css_selector('input[id$=lastName]')
        current_button.send_keys(self.lastname)
        
        #Enters Address
        self.dbgr.debug("Entering Address")
        current_button = self.driver.find_element_by_css_selector('input[id$=street]')
        current_button.send_keys(self.address)
        
        #Enters City
        self.dbgr.debug("Entering City")
        current_button = self.driver.find_element_by_css_selector('input[id$=city]')
        current_button.send_keys(self.city)
        
        #Enters State
        self.dbgr.debug("Entering State")
        current_button = self.driver.find_element_by_name("state") #wont find with css for some reason
        current_button.send_keys(self.state)
        
        #Enters Zipcode
        self.dbgr.debug("Entering Zipcode")
        current_button = self.driver.find_element_by_css_selector('input[id$=zipcode]')
        current_button.send_keys(self.zipcode)

        if glv.GUEST:
            self.dbgr.debug("Entering Email")
            current_button = self.driver.find_element_by_id("user.emailAddress")
            current_button.send_keys(self.username)

            self.dbgr.debug("Entering Phone Number")
            current_button = self.driver.find_element_by_id("user.phone")
            current_button.send_keys(self.pn)
        
        #Clicks 'Continue to Payment Information'
        self.dbgr.debug("Clicking 'Continue to Payment Information'")
        current_button = self.driver.find_element_by_class_name("btn-secondary")
        current_button.click()

        #check for next elenement before continuing

    def paymentInfo(self):
        self.dbgr.debug("---Payment Info:")
        
        #Enter Credit Card information
        self.dbgr.debug("Entering Card Number")
        current_button = self.driver.find_element_by_id("optimized-cc-card-number")
        current_button.send_keys(self.card)
        
        #Enter Month
        self.dbgr.debug("Entering Month")
        current_button = self.driver.find_element_by_name("expiration-month")
        current_button.send_keys(self.expmonth)
        
        #Enter Year
        self.dbgr.debug("Entering Year")
        current_button = self.driver.find_element_by_name("expiration-year")
        current_button.send_keys(self.expyear)
        
        #Enter CCV
        self.dbgr.debug("Entering CCV")
        current_button = self.driver.find_element_by_id("credit-card-cvv")
        current_button.send_keys(self.cvv)

        #check for next element before continuing
    
    def buyItem(self):        
        #place order
        self.dbgr.debug("Clicking 'Purchase'")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

        #TODO check for success/failure. return True on success, False for failure
        purchasing.purchaseSuccess()
        self.dbgr.debug("Purchase successful.")
        return True
        

