from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg
import time
import traceback
import chromedriver_binary
from company import company

class bestbuy(company):
    pass


        
    
    def purchase(self, link):
        self.driver.get(link)
        
        running = True
        while running:
            self.dbgr.debug("Starting Program")
            try:
                #add to cart
                self.addToCart()

                #checkout()
                self.checkout()  

                #Enter Shipping Info
                self.shippingInfo()

                #Enter Payment Info
                self.paymentInfo()
                
                #self.driver.close
                break
            except:
                self.dbgr.debug("Program failed: " + traceback.format_exc())
                time.sleep(30)
                #self.driver.close
                break
    
    def addToCart(self):
        current_button = self.driver.find_element_by_class_name("add-to-cart-button")
        self.dbgr.debug("Found add-to-cart button")

        if(current_button.get_attribute("data-button-state")) == "SOLD_OUT":
            self.dbgr.debug("item is sold out, retrying in 10")
            #continue
        self.dbgr.debug("item is not sold out, trying to add to cart")
        
        #Clicks the add-cart button
        self.dbgr.debug("Clicking the add-to-cart button")
        current_button.click()

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
        self.dbgr.debug("Clicking the go-to-cart button")
        current_button = self.driver.find_element_by_class_name("c-button-block")
        current_button.click()

    def checkout(self):
        #Clicks the checkout button
        self.dbgr.debug("Clicking the checkout button")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()

    def shippingInfo(self):
        #Enter Username 
        self.dbgr.debug("Entering Username")
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

        #Enters Firstname
        self.dbgr.debug("Entering Firstname")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.firstName")
        current_button.send_keys(self.firstname)
        
        #Enters Lastname
        self.dbgr.debug("Entering Lastname")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.lastName")
        current_button.send_keys(self.lastname)
        
        #Enters Address
        self.dbgr.debug("Entering Address")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.street")
        current_button.send_keys(self.address)
        
        #Enters City
        self.dbgr.debug("Entering City")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.city")
        current_button.send_keys(self.city)
        
        #Enters State
        self.dbgr.debug("Entering State")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.state")
        current_button.send_keys(self.state)
        
        #Enters Zipcode
        self.dbgr.debug("Entering Zipcode")
        current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1153.zipcode")
        current_button.send_keys(self.zipcode)
        
        #Clicks 'Continue to Payment Information'
        self.dbgr.debug("Clicking 'Continue to Payment Information'")
        current_button = self.driver.find_element_by_class_name("btn-secondary")
        current_button.click()

    def paymentInfo(self):
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
        
        #place order
        self.dbgr.debug("Clicks Purchase")
        current_button = self.driver.find_element_by_class_name("btn-primary")
        current_button.click()
        
