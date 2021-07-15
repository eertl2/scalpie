import glv
import os

from datetime import date
from datetime import datetime

class dbgr:
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
        threadid = "[PID:" + str(os.getpid()) + "] " #add thread to debug
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
        cr = open("logs/" + self.fdrname + "/" + self.flename + "_source.txt", "wb")
        cr.write(arg1.encode('cp1252', errors='ignore'))
        return