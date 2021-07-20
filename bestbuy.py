from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from company import company

import glv
import dbg
import time
import traceback
import random
import chromedriver_binary

dbg = dbg.dbgr()

class bestbuy(company):
    pass
    
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
            if glv.PRINT_SCREENSHOT:
                dbg.screenshot(self.driver)
            self.driver.close
            raise

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

        while(current_button.get_attribute("data-button-state") == "SOLD_OUT" or \
                current_button.get_attribute("data-button-state")) == "IN_STORE_ONLY":
            self.dbgr.debug("item is sold out, retrying in ~10")
            time.sleep(random.randint(glv.MIN_REFRESH_TIME,glv.MAX_REFRESH_TIME))
            self.driver.refresh
            continue
        
        #Clicks the add-cart button
        #dbg.debug("Clicking the add-to-cart button")
        #current_button.click()

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        #TODO: Make this robust, current iteration would fail Bestbuy's queuing system
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

        #check for next element before continuing
        current_button = self.driver.find_element_by_class_name("checkout-buttons__checkout")

    def checkout(self):
        dbg.debug("---Checkout:")

        #Clicks the checkout button
        dbg.debug("Clicking 'Checkout'")
        current_button = self.driver.find_element_by_class_name("checkout-buttons__checkout")
        current_button.click()

        #check for next element before continuing
        current_button = self.driver.find_element_by_class_name("cia-guest-content__continue") 


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

            #check for next element before continuing
            current_button = self.driver.find_element_by_css_selector('input[id$=firstName]')


    def shippingInfo(self):
        dbg.debug("---Shipping Info:")
        #Enters Firstname
        dbg.debug("Entering Firstname")
        current_button = self.driver.find_element_by_css_selector('input[id$=firstName]')
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.firstname)
        
        #Enters Lastname
        dbg.debug("Entering Lastname")
        current_button = self.driver.find_element_by_css_selector('input[id$=lastName]')
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.lastname)
        
        #Enters Address
        dbg.debug("Entering Address")
        current_button = self.driver.find_element_by_css_selector('input[id$=street]')
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.address)
        
        #Enters City
        dbg.debug("Entering City")
        current_button = self.driver.find_element_by_css_selector('input[id$=city]')
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.city)
        
        #Enters State
        dbg.debug("Entering State")
        current_button = self.driver.find_element_by_name("state") #wont find with css for some reason
        current_button.send_keys(self.state)
        
        #Enters Zipcode
        dbg.debug("Entering Zipcode")
        current_button = self.driver.find_element_by_css_selector('input[id$=zipcode]')
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.zipcode)

        if glv.GUEST:
            dbg.debug("Entering Email")
            current_button = self.driver.find_element_by_id("user.emailAddress")
            current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            current_button.send_keys(self.username)

            dbg.debug("Entering Phone Number")
            current_button = self.driver.find_element_by_id("user.phone")
            current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
            current_button.send_keys(self.pn)
        
        #Clicks 'Continue to Payment Information'
        dbg.debug("Clicking 'Continue to Payment Information'")
        current_button = self.driver.find_element_by_class_name("btn-secondary")
        current_button.click()

        #check for next elenement before continuing
        current_button = self.driver.find_element_by_id("optimized-cc-card-number")

    def paymentInfo(self):
        dbg.debug("---Payment Info:")
        
        #Enter Credit Card information
        dbg.debug("Entering Card Number")
        current_button = self.driver.find_element_by_id("optimized-cc-card-number")
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.card)
        
        #Enter Month
        dbg.debug("Entering Month")
        current_button = self.driver.find_element_by_name("expiration-month")
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.expmonth)
        
        #Enter Year
        dbg.debug("Entering Year")
        current_button = self.driver.find_element_by_name("expiration-year")
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.expyear)
        
        #Enter CCV
        dbg.debug("Entering CCV")
        current_button = self.driver.find_element_by_id("credit-card-cvv")
        current_button.send_keys(Keys.CONTROL + 'a' + Keys.DELETE)
        current_button.send_keys(self.cvv)

        #check for next element before continuing
        current_button = self.driver.find_element_by_class_name("btn-primary")
    
    def buyItem(self):        
        #place order
        dbg.debug("Clicking 'Purchase'")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

        #TODO check for success/failure. return True on success, False for failure
        return True

    def close(self):
        self.driver.close
        

