from bestbuy import BestBuy
from task import Task

import dbg
import time

dbg = dbg.Dbg()

class Worker:
    def __init__(self, platform, link, task):
        self.platform = platform
        self.task = task
        self.link = link
        self.company = self.refresh(platform, link)
        self.finished = False
        
        self.run()

    def run(self):
        while not self.finished:
            try:
                self.company.purchase()

                dbg.debug("Aquiring Purchase Perm")
                
                while(Task.acquirePurchasePerm(self.task) != 1):
                    dbg.debug("Waiting for buying permission")
                    if(Task.acquirePurchasePerm(self.task) == -1):
                        dbg.debug("Max quanity of product has already been bought")
                        self.finished = True
                        return
                    time.sleep(5)
                
                dbg.debug("Aquired Purchase Perm. Buying item...")
                    
                if self.company.buyItem():
                    self.company.screenshot()
                    self.finished = True
            except:
                dbg.debug("worker failed, retrying...")
                self.company = self.refresh(self.platform, self.link)

    def refresh(self, platform, link):
        if platform == "bestbuy":
            return BestBuy(link)
        else:
            raise platformDoesntExist(platform)
    
class platformDoesntExist(Exception):
    def __init__(self, platform):
        super().__init__("platform [" + platform + "] does not exist")
