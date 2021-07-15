from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
import glv
import dbg

import chromedriver_binary

class company:
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
        op = wd.ChromeOptions()
        if glv.HIDE_CHROME:
            op.add_argument('--headless')
            op.add_argument('--no-proxy-server') 
            op.add_argument("--window-size=1920,1080")
            op.add_argument("--proxy-server='direct://'")
            op.add_argument("--proxy-bypass-list=*")
            op.add_argument('--disable-dev-shm-usage')
        self.driver = wd.Chrome(options=op)
        self.driver.implicitly_wait(10)
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