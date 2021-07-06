from selenium import webdriver as wd
import chromedriver_binary

#Adds just dance to cart on bestbuy

wd = wd.Chrome()
wd.implicitly_wait(10)

wd.get("https://www.bestbuy.com/site/just-dance-2021-playstation-5/6427617.p?skuId=6427617")

cartButton = wd.find_element_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button")

cartButton.click()

