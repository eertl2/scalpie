import bestbuy
import glv
import dbg
import time

dbg = dbg.dbgr()

class worker:
    def __init__(self, place, item, lock, activeP, purchased):
        if place == "bestbuy":
            bb = bestbuy.bestbuy()     
            bb.purchase(item) #brings browser to the 'buy now' button, but program has to get permission first
            pcode = self.acquirePurchasePerm(lock, activeP, purchased)
            z = 0
            while(pcode == 0):
                dbg.debug("Waiting for buying permission")
                z += 1
                if z == 5:
                    dbg.debug("timeout")
                    return
                time.sleep(5)
                pcode = self.acquirePurchasePerm(lock, activeP, purchased)
                if(pcode == -1):
                    dbg.debug("Max quanity of product has already been bought")
                    return
            if(bb.buyItem()):
                self.purchaseSuccess(lock, activeP, purchased)
                dbg.debug("Purchase successful.")
            else:
                self.purchaseFail(lock, activeP, purchased)
                dbg.debug("Purchase Failed.")
            bb.close()

    def acquirePurchasePerm(self, lock, activeP, purchased):
        with lock:
            if(activeP.value + purchased.value) < glv.QUANITY:
                activeP.value += 1
                return 1
            if(purchased.value == glv.QUANITY):
                return -1
        return 0
    
    def purchaseSuccess(self, lock, activeP, purchased):
        with lock:
            activeP.value -= 1
            purchased.value += 1

    def purchaseFail(self, lock, activeP, purchased):
        with lock:
            activeP.value -= 1