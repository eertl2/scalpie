from concurrent.futures import ThreadPoolExecutor as pool
from concurrent.futures import as_completed

from bestbuy import BestBuy
from threading import Lock
import glv
import dbg
import time
import tasklist

dbg = dbg.Dbg()

class Worker:
    def __init__(self, task):
        self.activeP = 0
        self.purchased = 0
        self.lock = Lock()
        self.task = task

        with pool() as executor:
            futures = [executor.submit(BestBuy, link) for link in task.links]

            for buyer in as_completed(futures): #buyer is a future instance that is ready to buy an item
                while(not self.acquirePurchasePerm()):
                    dbg.debug("Waiting for buying permission")
                    time.sleep(5)

                dbg.debug("Got buying permission. Buying item")

                if buyer.result().buyItem(): #only one buyer can buy at a time, all other future instances are held until this goes through
                    if self.checkComplete(True):
                        self.task.completed = True
                        dbg.debug("Worker should be finished!")
                        executor.shutdown()
                else:
                    self.checkComplete(False)

    def acquirePurchasePerm(self):
        with self.lock:
            if(self.activeP + self.purchased) < self.task.amt:
                self.activeP += 1 
                return True #green-light to try purchasing
            return False


    def checkComplete(self, success):
        with self.lock:
            self.activeP -= 1 #buyer completed, decrement active buyers
            
            if success:
                self.purchased += 1 #item was a success
                if(self.purchased == self.task.amt):
                    return True
                else:
                    return False
                

