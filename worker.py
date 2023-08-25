from concurrent.futures import ThreadPoolExecutor as pool
from concurrent.futures import as_completed
from bestbuy import BestBuy
from threading import Lock

import dbg
import time

dbg = dbg.Dbg()

class Worker:
    def __init__(self, task):
        self.activeP = 0
        self.purchased = 0
        self.lock = Lock()
        self.task = task
        self.run(task)

    def run(self, task):
        with pool() as executor:
            futures = [executor.submit(BestBuy, link) for link in task.links]

            for buyer in futures: #buyer is a future instance that is ready to buy an item
                try:
                    buyer.result()
                except:
                    dbg.debug("Buyer" + str(futures.index(buyer)) + "failed")
                    continue

                while(self.acquirePurchasePerm() != 1):
                    dbg.debug("Waiting for buying permission")
                    if(self.acquirePurchasePerm() == -1):
                        dbg.debug("Max quanity of product has already been bought")
                        return
                    time.sleep(5)

                dbg.debug("Got buying permission. Buying item")

                purchaser = executor.submit(buyer.result().buyItem())

                for purchased in as_completed(purchaser):
                    if purchased:
                        if self.checkComplete(True):
                            self.task.completed = True
                            dbg.debug("Worker should be finished!")
                    else:
                        self.checkComplete(False)

    def acquirePurchasePerm(self):
        with self.lock:
            if(self.activeP + self.purchased) < self.task.amt:
                self.activeP += 1 
                return 1 #green-light to try purchasing
            if( self.purchased == self.task.amt):
                return -1
            return 0


    def checkComplete(self, success):
        with self.lock:
            self.activeP -= 1 #buyer completed, decrement active buyers
            
            if success:
                self.purchased += 1 #item was a success
                if(self.purchased == self.task.amt):
                    return True
                else:
                    return False
                

