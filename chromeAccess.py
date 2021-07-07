from selenium import webdriver as wd
import time
import chromedriver_binary

#Adds just dance to cart on bestbuy

wd = wd.Chrome()
wd.implicitly_wait(10)

wd.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

running = True
success = False

while running:
    try:
        time.sleep(10)
        wd.refresh()
        cartbutton = wd.find_element_by_class_name("add-to-cart-button")

        print("element found...")
        #cartButton.click()
        if(cartbutton.get_attribute("data-button-state")) == "SOLD_OUT":
            print("item is sold out, retrying in 10")
            continue
        break
    except:
        print("failed to find element...retrying in 10")
        continue



