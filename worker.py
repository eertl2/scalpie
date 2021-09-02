from bestbuy import BestBuy

import dbg

dbg = dbg.Dbg()

class Worker:
    def __init__(self, platform, link, scheduler):
        self.platform = platform
        self.scheduler = scheduler
        self.link = self.link
        self.company = self.refresh(platform, link)
        self.finished = False #only True if the item is bought
        
        self.run()

    def run(self):
        while not self.finished:
            try:
                self.company.purchase()
                #get lock from scheduler
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
