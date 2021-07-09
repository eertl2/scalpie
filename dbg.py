import glv
import os
from datetime import date
from datetime import datetime

class dbgr:
    f = None

    def __init__(self):
        if not os.path.exists('logs'):
            os.makedirs('logs')
        if(glv.printToLogs):
            fdrname = date.today().strftime("%d_%m_%Y")
            if not os.path.exists("logs/" + fdrname):
                os.makedirs("logs/" + fdrname)
            flename = datetime.now().strftime("%H_%M_%S")
            self.f = open("logs/" + fdrname + "/" + flename + ".txt","a")

    def debug(self, arg1):
        if glv.printToConsole:
            print(arg1)
        if glv.printToLogs:
            self.log(arg1)
        return

    def log(self, arg1):
        datestamp = datetime.now().strftime("[%H:%M:%S] ")
        self.f.write(datestamp + arg1 + "\n")
        return