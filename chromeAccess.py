from selenium import webdriver as wd
import time
import chromedriver_binary

#Adds just dance to cart on bestbuy

wd = wd.Chrome()
wd.implicitly_wait(10) 

#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
wd.get("https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286") #test-item (in-stock)

#User-details
username = "superdreaddragon@gmail.com"
password = "YuQMCfe-4is3!KB"
firstname = "Eric"
lastname = "Ertl"
address = "N42W22630 Cabot Ct"
city = "Pewaukee"
state = "WI"
zipcode = "53072"
card = "5482283375750932"
expmonth = "03"
expyear = "2023"
cvv = "003"

running = True
#success = False

while running:
    try:
        time.sleep(3)
        wd.refresh()
        cartbutton = wd.find_element_by_class_name("add-to-cart-button")

        print("element found...")

        if(cartbutton.get_attribute("data-button-state")) == "SOLD_OUT":
            print("item is sold out, retrying in 10")
            continue
        
        print("item is not sold out, trying to add to cart")
        
        #Clicks the add-cart button
        cartbutton.click()
        print("Clicking the add-to-cart button")

        #Clicks the go-to-cart button
        cartbutton = wd.find_element_by_class_name("c-button-block")
        cartbutton.click()
        print("Clicking the go-to-cart button")

        #Clicks the checkout button
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()
        print("Clicking the checkout button")

        #Enter Username 
        cartbutton = wd.find_element_by_id("fld-e")
        cartbutton.send_keys(username)

        #Enter Password
        cartbutton = wd.find_element_by_id("fld-p1")
        cartbutton.send_keys(password)

        #Clicks login
        cartbutton = wd.find_element_by_class_name("cia-form__controls__submit")
        cartbutton.click()
        print("Clicking the login button")

        #Enters Firstname
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.firstName")
        cartbutton.send_keys(firstname)

        #Enters Lastname
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.lastName")
        cartbutton.send_keys(lastname)

        #Enters Address
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.street")
        cartbutton.send_keys(address)

        #Enters City
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.city")
        cartbutton.send_keys(city)

        #Enters State
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.state")
        cartbutton.send_keys(state)

        #Enters Zipcode
        cartbutton = wd.find_element_by_id("consolidatedAddresses.ui_address_1154.zipcode")
        cartbutton.send_keys(zipcode)

        #Clicks 'Continue to Payment Information'
        cartbutton = wd.find_element_by_class_name("btn-secondary")
        cartbutton.click()
        print("Clicks 'Continue to Payment Information'")

        #Enter Credit Card information
        cartbutton = wd.find_element_by_id("optimized-cc-card-number")
        cartbutton.send_keys(card)

        #Enter Month
        cartbutton = wd.find_element_by_name("expiration-month")
        cartbutton.send_keys(expmonth)

        #Enter Year
        cartbutton = wd.find_element_by_name("expiration-year")
        cartbutton.send_keys(expyear)

        #Enter Credit Card information
        cartbutton = wd.find_element_by_id("credit-card-cvv")
        cartbutton.send_keys(cvv)

        #place order
        cartbutton = wd.find_element_by_class_name("btn-primary")
        cartbutton.click()
        print("Clicks Purchase")

        break
    except:
        print("failed to find element")
        break




