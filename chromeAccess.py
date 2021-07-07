from selenium import webdriver as wd
import time
import chromedriver_binary # type: ignore

lines = []
userdata = []
with open('user-details.txt') as f:
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

#count = 0
#for p in userdata:
#    print(f'line {count}: {p}')
#    count += 1

wd = wd.Chrome()
wd.implicitly_wait(10) 

#wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149") #ps5
wd.get("https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286") #test-item (in-stock)

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

        #Needs to wait in queue until we are able to add-to-cart if we get a popup
        #if(cartbutton.get_attribute(""))

            #Must click the button as it becomes available

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




