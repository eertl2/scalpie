from selenium import webdriver as wd
import chromedriver_binary

#Adds just dance to cart on bestbuy

wd = wd.Chrome()
wd.implicitly_wait(10)

wd.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")

try:
    cartButton = wd.find_element_by_class_name("add-to-cart-button")
    print(cartButton.get_attribute("data-button-state"))
except:
    print("failed to find element")

