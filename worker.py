import bestbuy
import glv
import dbg
import time

dbg = dbg.dbgr()

class worker:
    def __init__(self, place, item, lock, activeP, purchased):
        if place == "bestbuy":
            bb = bestbuy.bestbuy()     
            if(bb.purchase(item)):
                pcode = self.acquirePurchasePerm(lock, activeP, purchased)
                while(pcode == 0):
                    dbg.debug("Waiting for buying permission")
                    time.sleep(5)
                    pcode = self.acquirePurchasePerm(lock, activeP, purchased)
                    if(pcode == -1):
                        dbg.debug("Max quanity of product has already been bought")
                        return

    def acquirePurchasePerm(self, lock, activeP, purchased):
        with lock:
            if(activeP.value + purchased.value) < glv.QUANITY:
                activeP.value += 1
                return 1
            if(purchased.value == glv.QUANITY):
                return -1
            return 0
    
    def purchaseSuccess(self, lock, purchased):
        with lock:
            purchased += 1