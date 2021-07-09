from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg
import time
import traceback
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
    driver = None
    dbgr = None

    def __init__(self):
        self.driver = wd.Chrome()
        self.driver.implicitly_wait(15)
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
    
    def purchase(self, link):
        self.driver.get(link)
        
        running = True
        while running:
            self.dbgr.debug("Starting Program")
            try:
                time.sleep(3)
                self.driver.refresh()
                current_button = self.driver.find_element_by_class_name("add-to-cart-button")

                self.dbgr.debug("Found add-to-cart button")

                if(current_button.get_attribute("data-button-state")) == "SOLD_OUT":
                    self.dbgr.debug("item is sold out, retrying in 10")
                    continue
                
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
                time.sleep(3)

                #Clicks the checkout button
                self.dbgr.debug("Clicking the checkout button")
                current_button = self.driver.find_element_by_class_name("btn-primary")
                current_button.click()
                time.sleep(3)

                #Enter Username 
                self.dbgr.debug("Entering Username")
                current_button = self.driver.find_element_by_id("fld-e")
                current_button.send_keys(self.username)
                time.sleep(3)
                

                #Enter Password
                self.dbgr.debug("Entering Password")
                current_button = self.driver.find_element_by_id("fld-p1")
                current_button.send_keys(self.password)
                time.sleep(3)

                #Clicks login
                # self.dbgr.debug("Clicking the login button")
                # current_button = self.driver.find_element_by_class_name("cia-form__controls__submit")
                # current_button.click()
                # time.sleep(3)

                #Enters Firstname
                self.dbgr.debug("Entering Firstname")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.firstName")
                current_button.send_keys(self.firstname)
                time.sleep(3)

                #Enters Lastname
                self.dbgr.debug("Entering Lastname")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.lastName")
                current_button.send_keys(self.lastname)
                time.sleep(3)

                #Enters Address
                self.dbgr.debug("Entering Address")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.street")
                current_button.send_keys(self.address)
                time.sleep(3)

                #Enters City
                self.dbgr.debug("Entering City")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.city")
                current_button.send_keys(self.city)
                time.sleep(3)

                #Enters State
                self.dbgr.debug("Entering State")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.state")
                current_button.send_keys(self.state)
                time.sleep(3)

                #Enters Zipcode
                self.dbgr.debug("Entering Zipcode")
                current_button = self.driver.find_element_by_id("consolidatedAddresses.ui_address_1154.zipcode")
                current_button.send_keys(self.zipcode)
                time.sleep(3)

                #Clicks 'Continue to Payment Information'
                self.dbgr.debug("Clicking 'Continue to Payment Information'")
                current_button = self.driver.find_element_by_class_name("btn-secondary")
                current_button.click()
                time.sleep(3)

                #Enter Credit Card information
                self.dbgr.debug("Entering Card Number")
                current_button = self.driver.find_element_by_id("optimized-cc-card-number")
                current_button.send_keys(self.card)
                time.sleep(3)

                #Enter Month
                self.dbgr.debug("Entering Month")
                current_button = self.driver.find_element_by_name("expiration-month")
                current_button.send_keys(self.expmonth)
                time.sleep(3)

                #Enter Year
                self.dbgr.debug("Entering Year")
                current_button = self.driver.find_element_by_name("expiration-year")
                current_button.send_keys(self.expyear)
                time.sleep(3)

                #Enter CCV
                self.dbgr.debug("Entering CCV")
                current_button = self.driver.find_element_by_id("credit-card-cvv")
                current_button.send_keys(self.cvv)
                time.sleep(3)

                #place order
                self.dbgr.debug("Clicks Purchase")
                current_button = self.driver.find_element_by_class_name("btn-primary")
                current_button.click()
                time.sleep(3)

                self.driver.close
                break
            except:
                self.dbgr.debug("Program failed: " + traceback.format_exc())
                self.driver.close
                break
