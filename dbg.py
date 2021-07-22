import glv
import os
import threading
import chromedriver_binary # not needed?

from datetime import date
from datetime import datetime

class Dbg:
    f = None
    fdrname = None
    flename = None

    def __init__(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if(glv.PRINT_TO_LOGS):
            self.fdrname = date.today().strftime("%d_%m_%Y")
            if not os.path.exists("logs/" + self.fdrname):
                os.makedirs("logs/" + self.fdrname)
            self.flename = datetime.now().strftime("%H_%M")
            self.f = open("logs/" + self.fdrname + "/" + self.flename + ".txt","a")

    def debug(self, arg1):
        threadid = "[ID:" + str(threading.get_ident()) + "] " #add thread to debug
        datestamp = datetime.now().strftime("[%H:%M:%S] ") #add date to debug
        arg1 = threadid + datestamp + arg1

        if glv.PRINT_TO_LOGS:
            print(arg1)
        if glv.PRINT_TO_LOGS:
            self.log(arg1)
        return

    def log(self, arg1):
        self.f.write(arg1 + "\n")
        return

    def crash(self, arg1):
        cr = open("logs/" + self.fdrname + "/" + self.flename + "_pg_" + str(threading.get_ident()) + ".txt", "wb")
        cr.write(arg1.encode('cp1252', errors='ignore'))
        return

    def screenshot(self, wd):
        wd.maximize_window()
        wd.save_screenshot("logs/" + self.fdrname + "/" + self.flename + "_ss_" + str(threading.get_ident()) + ".png")
